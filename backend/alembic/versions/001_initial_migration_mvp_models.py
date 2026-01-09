"""Initial migration - MVP models

Revision ID: 001
Revises: 
Create Date: 2026-01-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criar tabela users
    op.create_table(
        'users',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('subscription', sa.Enum('FREE', 'PREMIUM', name='subscriptiontype'), nullable=False, server_default='FREE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    # Criar tabela professor_profiles
    op.create_table(
        'professor_profiles',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('professor_name', sa.String(), nullable=False),
        sa.Column('personality', sa.Enum('MOTIVADOR', 'PACIENTE', 'DESAFIADOR', 'AMIGAVEL', name='personalitytype'), nullable=False),
        sa.Column('subject', sa.Enum('TODAS', 'PORTUGUES', 'MATEMATICA', 'HISTORIA', 'GEOGRAFIA', 'CIENCIAS', 'BIOLOGIA', 'FISICA', 'QUIMICA', 'INGLES', 'ESPANHOL', 'ARTES', 'EDUCACAO_FISICA', 'FILOSOFIA', 'SOCIOLOGIA', name='subjecttype'), nullable=False),
        sa.Column('level', sa.Enum('INICIANTE', 'INTERMEDIARIO', 'AVANCADO', name='leveltype'), nullable=False),
        sa.Column('interests', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('hobbies', sa.String(), nullable=True),
        sa.Column('goal', sa.String(), nullable=True),
        sa.Column('favorite_subjects', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_professor_profiles_user_id'), 'professor_profiles', ['user_id'], unique=False)
    
    # Criar tabela conversations
    op.create_table(
        'conversations',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('profile_id', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('subject', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('last_message_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['profile_id'], ['professor_profiles.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_conversations_user_id'), 'conversations', ['user_id'], unique=False)
    op.create_index(op.f('ix_conversations_profile_id'), 'conversations', ['profile_id'], unique=False)
    
    # Criar tabela messages
    op.create_table(
        'messages',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('conversation_id', sa.String(), nullable=False),
        sa.Column('role', sa.Enum('USER', 'ASSISTANT', name='messagerole'), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('message_metadata', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_conversation_id'), 'messages', ['conversation_id'], unique=False)
    
    # Criar tabela progress
    op.create_table(
        'progress',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('subject', sa.String(), nullable=False),
        sa.Column('xp', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('level', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('streak', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('last_study_date', sa.DateTime(timezone=True), nullable=True),
        sa.Column('badges', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_progress_user_id'), 'progress', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_progress_user_id'), table_name='progress')
    op.drop_table('progress')
    op.drop_index(op.f('ix_messages_conversation_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_conversations_profile_id'), table_name='conversations')
    op.drop_index(op.f('ix_conversations_user_id'), table_name='conversations')
    op.drop_table('conversations')
    op.drop_index(op.f('ix_professor_profiles_user_id'), table_name='professor_profiles')
    op.drop_table('professor_profiles')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    
    # Dropar enums
    sa.Enum(name='subscriptiontype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='personalitytype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='subjecttype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='leveltype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='messagerole').drop(op.get_bind(), checkfirst=True)
