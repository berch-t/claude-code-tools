#!/usr/bin/env node
/**
 * {{SERVER_NAME}} MCP Server
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
  Tool,
  TextContent,
} from '@modelcontextprotocol/sdk/types.js';

const server = new Server(
  {
    name: '{{SERVER_NAME}}',
    version: '{{VERSION}}',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Example tool
const exampleTool: Tool = {
  name: 'example_tool',
  description: 'An example tool for {{SERVER_NAME}}',
  inputSchema: {
    type: 'object',
    properties: {
      message: {
        type: 'string',
        description: 'A message to process',
      },
    },
    required: ['message'],
  },
};

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [exampleTool],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'example_tool') {
    const { message } = args;
    return {
      content: [
        {
          type: 'text',
          text: `{{SERVER_NAME}} processed: ${message}`,
        } as TextContent,
      ],
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('{{SERVER_NAME}} MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});