/**
 * MCP Servers Configuration for Educational Platform
 * 
 * This file configures all MCP (Model Context Protocol) servers
 * using Nx's configureMcpServer API.
 * 
 * Organized by tiers:
 * - Tier 1: Essential servers (5)
 * - Tier 2: Expansion servers (4)
 * - Tier 3: Optimization servers (3)
 */

// Import Nx configuration function if available
// import { configureMcpServer } from '@nx/mcp';

/**
 * Tier 1: Essential MCP Servers
 */
const tier1Servers = {
  // 1. Backend - Supabase
  supabase: {
    name: 'supabase',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-supabase'],
    env: {
      SUPABASE_URL: process.env.SUPABASE_URL || '',
      SUPABASE_KEY: process.env.SUPABASE_KEY || '',
      SUPABASE_SERVICE_ROLE_KEY: process.env.SUPABASE_SERVICE_ROLE_KEY || '',
    },
  },

  // 2. Matemática - SymPy / Scientific Calculator
  'scientific-calculator': {
    name: 'scientific-calculator',
    command: 'python3',
    args: ['-m', 'mcp_scientific_calculator'],
    env: {},
    // Note: Requires installation of:
    // pip install sympy numpy scipy pandas mcp-scientific-calculator
    // See: _docs/CONFIGURACAO-SYMPY-MCP.md for detailed setup
  },

  // 3. Visualização - Desmos / Plotly
  desmos: {
    name: 'desmos',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-desmos'],
    env: {
      DESMOS_API_KEY: process.env.DESMOS_API_KEY || '',
    },
  },

  plotly: {
    name: 'plotly',
    command: 'python',
    args: ['-m', 'mcp_server_plotly'],
    env: {},
  },

  // 4. Aprendizagem - Anki
  anki: {
    name: 'anki',
    command: 'python',
    args: ['-m', 'mcp_server_anki'],
    env: {
      ANKI_CONNECT_URL: 'http://localhost:8765',
    },
  },

  // 5. Avaliação - Homework Grading
  'homework-grading': {
    name: 'homework-grading',
    command: 'python',
    args: ['-m', 'mcp_server_homework_grading'],
    env: {
      OPENAI_API_KEY: process.env.OPENAI_API_KEY || '',
      GRADING_MODEL: 'gpt-4o',
    },
  },
};

/**
 * Tier 2: Expansion MCP Servers
 */
const tier2Servers = {
  // 6. Integração LMS - Moodle
  moodle: {
    name: 'moodle',
    command: 'python',
    args: ['-m', 'mcp_server_moodle'],
    env: {
      MOODLE_URL: process.env.MOODLE_URL || '',
      MOODLE_TOKEN: process.env.MOODLE_TOKEN || '',
    },
  },

  // 7. Integração LMS - Canvas
  canvas: {
    name: 'canvas',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-canvas'],
    env: {
      CANVAS_API_URL: process.env.CANVAS_API_URL || '',
      CANVAS_API_TOKEN: process.env.CANVAS_API_TOKEN || '',
    },
  },

  // 8. Ecossistema - Google Classroom
  'google-classroom': {
    name: 'google-classroom',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-google-classroom'],
    env: {
      GOOGLE_CLIENT_ID: process.env.GOOGLE_CLIENT_ID || '',
      GOOGLE_CLIENT_SECRET: process.env.GOOGLE_CLIENT_SECRET || '',
      GOOGLE_REDIRECT_URI: 'http://localhost:3000/oauth/callback',
    },
  },

  // 9. Ecossistema - Google Drive
  'google-drive': {
    name: 'google-drive',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-google-drive'],
    env: {
      GOOGLE_CLIENT_ID: process.env.GOOGLE_CLIENT_ID || '',
      GOOGLE_CLIENT_SECRET: process.env.GOOGLE_CLIENT_SECRET || '',
      GOOGLE_REDIRECT_URI: 'http://localhost:3000/oauth/callback',
    },
  },

  // 10. Automação - Zapier
  zapier: {
    name: 'zapier',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-zapier'],
    env: {
      ZAPIER_API_KEY: process.env.ZAPIER_API_KEY || '',
    },
  },

  // 11. Multimídia - MiniMax
  minimax: {
    name: 'minimax',
    command: 'python',
    args: ['-m', 'mcp_server_minimax'],
    env: {
      MINIMAX_API_KEY: process.env.MINIMAX_API_KEY || '',
      MINIMAX_GROUP_ID: process.env.MINIMAX_GROUP_ID || '',
    },
  },

  // 12. Design - Figma Make (Remote MCP Server)
  // Note: Remote server uses SSE transport (Server-Sent Events)
  // For Cursor, configure in .cursor/mcp.json:
  // {
  //   "figma-remote": {
  //     "url": "https://mcp.figma.com/mcp",
  //     "transport": "sse"
  //   }
  // }
  // Authentication: OAuth flow handled in Figma Dev Mode
  // See: _docs/CONFIGURACAO-FIGMA-MAKE-MCP.md for detailed setup
  'figma-remote': {
    name: 'figma-remote',
    // Configured via JSON in .cursor/mcp.json (see documentation)
    // URL: https://mcp.figma.com/mcp
    // Transport: SSE
  },
};

/**
 * Tier 3: Optimization MCP Servers
 */
const tier3Servers = {
  // 13. Design - Figma Make (Desktop MCP Server)
  'figma-desktop': {
    name: 'figma-desktop',
    command: 'npx',
    args: ['-y', '@figma/mcp-server'],
    env: {
      // Desktop server uses local connection to Figma app
      FIGMA_DESKTOP_PORT: process.env.FIGMA_DESKTOP_PORT || '5555',
    },
  },

  // 14. Programação - E2B
  e2b: {
    name: 'e2b',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-e2b'],
    env: {
      E2B_API_KEY: process.env.E2B_API_KEY || '',
    },
  },

  // 15. Conteúdo - Firecrawl
  firecrawl: {
    name: 'firecrawl-mcp',
    command: 'npx',
    args: ['-y', 'firecrawl-mcp'],
    env: {
      FIRECRAWL_API_KEY: process.env.FIRECRAWL_API_KEY || 'fc-d9e38b1898aa4067be99276054db16be',
    },
  },

  // 16. Conteúdo - Browserbase
  browserbase: {
    name: 'browserbase',
    command: 'npx',
    args: ['-y', '@modelcontextprotocol/server-browserbase'],
    env: {
      BROWSERBASE_API_KEY: process.env.BROWSERBASE_API_KEY || '',
      BROWSERBASE_PROJECT_ID: process.env.BROWSERBASE_PROJECT_ID || '',
    },
  },

  // 17. Pesquisa - Exa
  exa: {
    name: 'exa',
    command: 'python',
    args: ['-m', 'mcp_server_exa'],
    env: {
      EXA_API_KEY: process.env.EXA_API_KEY || '',
    },
  },

  // 18. Pesquisa - AMiner
  aminer: {
    name: 'aminer',
    command: 'python',
    args: ['-m', 'mcp_server_aminer'],
    env: {
      AMINER_API_KEY: process.env.AMINER_API_KEY || '',
    },
  },
};

/**
 * Tier 4: Design & UI/UX MCP Servers
 */
const tier4Servers = {
  // Figma Make servers are in tier2 and tier3 above
};

/**
 * Tier 5: AI & ML MCP Servers
 */
const tier5Servers = {
  // Hugging Face MCP Server (Remote via SSE)
  // Note: Remote server uses SSE transport, configure directly in Cursor settings
  // URL: https://huggingface.co/mcp
  // Authentication: OAuth flow handled in Hugging Face settings
  // See: _docs/CONFIGURACAO-HUGGINGFACE-MCP.md for detailed setup
  huggingface: {
    name: 'huggingface',
    // Configured via JSON in .cursor/mcp.json (see documentation)
    // URL: https://huggingface.co/mcp
    // Transport: SSE
  },
};

/**
 * Combine all servers
 */
const allServers = {
  ...tier1Servers,
  ...tier2Servers,
  ...tier3Servers,
  ...tier4Servers,
  ...tier5Servers,
};

/**
 * Configure MCP servers using Nx API
 * 
 * Usage:
 * 1. Ensure you have Nx installed: npm install -g nx
 * 2. Run: nx configureMcpServer
 * 
 * Or use this configuration in Cursor settings
 */
export function configureMcpServers() {
  // If using Nx's configureMcpServer function
  // Object.values(allServers).forEach(server => {
  //   configureMcpServer(server);
  // });

  return allServers;
}

/**
 * Export server configurations for use in Cursor settings
 */
export const mcpServerConfig = configureMcpServers();

/**
 * Export individual tiers for selective configuration
 */
export { tier1Servers, tier2Servers, tier3Servers, tier4Servers, tier5Servers, allServers };

/**
 * Default export for easy import
 */
export default mcpServerConfig;

configureMcpServers