#!/usr/bin/env node
/**
 * {{SERVER_NAME}} MCP Server - TypeScript Implementation
 * 
 * {{DESCRIPTION}}
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  Tool,
  Prompt,
  Resource,
  TextContent,
  GetPromptResult,
  ReadResourceResult,
  CallToolResult,
} from '@modelcontextprotocol/sdk/types.js';

// Type definitions
interface ExampleToolArgs {
  message: string;
  count?: number;
}

interface ExamplePromptArgs {
  topic: string;
  style?: string;
}

/**
 * Initialize the MCP server
 */
const server = new Server(
  {
    name: '{{SERVER_NAME}}',
    version: '{{VERSION}}',
  },
  {
    capabilities: {
      tools: {},
      prompts: {},
      resources: {},
    },
  }
);

/**
 * Tool definitions
 */
const tools: Tool[] = [
  {
    name: 'example_tool',
    description: 'Example tool for {{SERVER_NAME}}',
    inputSchema: {
      type: 'object',
      properties: {
        message: {
          type: 'string',
          description: 'Message to process',
        },
        count: {
          type: 'number',
          description: 'Number of times to repeat',
          default: 1,
        },
      },
      required: ['message'],
    },
  },
  // Add more tools here
  {{ADDITIONAL_TOOLS}}
];

/**
 * Prompt definitions
 */
const prompts: Prompt[] = [
  {
    name: 'example_prompt',
    description: 'Example prompt for {{SERVER_NAME}}',
    arguments: [
      {
        name: 'topic',
        description: 'Topic to generate content about',
        required: true,
      },
      {
        name: 'style',
        description: 'Writing style to use',
        required: false,
      },
    ],
  },
  // Add more prompts here
  {{ADDITIONAL_PROMPTS}}
];

/**
 * Resource definitions
 */
const resources: Resource[] = [
  {
    uri: '{{SERVER_NAME}}://info',
    name: 'Server Information',
    description: 'Information about {{SERVER_NAME}}',
    mimeType: 'text/plain',
  },
  // Add more resources here
  {{ADDITIONAL_RESOURCES}}
];

/**
 * Tool handlers
 */
async function handleExampleTool(args: ExampleToolArgs): Promise<CallToolResult> {
  const { message, count = 1 } = args;

  // Validate inputs
  if (!message || typeof message !== 'string') {
    throw new Error('Message must be a non-empty string');
  }
  if (typeof count !== 'number' || count < 1 || count > 10) {
    throw new Error('Count must be between 1 and 10');
  }

  // Process the tool
  const result = Array(count).fill(message).join(' ');

  return {
    content: [
      {
        type: 'text',
        text: `{{SERVER_NAME}} processed: ${result}`,
      } as TextContent,
    ],
  };
}

// Add more tool handlers here
{{ADDITIONAL_TOOL_HANDLER_FUNCTIONS}}

/**
 * Prompt handlers
 */
async function handleExamplePrompt(args: ExamplePromptArgs): Promise<GetPromptResult> {
  const { topic, style = 'professional' } = args;

  if (!topic || typeof topic !== 'string') {
    throw new Error('Topic must be a non-empty string');
  }

  return {
    description: `Generate ${style} content about ${topic}`,
    messages: [
      {
        role: 'system',
        content: {
          type: 'text',
          text: `You are an expert writer creating ${style} content about ${topic}.`,
        },
      },
      {
        role: 'user',
        content: {
          type: 'text',
          text: `Write comprehensive content about ${topic} in a ${style} style.`,
        },
      },
    ],
  };
}

// Add more prompt handlers here
{{ADDITIONAL_PROMPT_HANDLER_FUNCTIONS}}

/**
 * Resource handlers
 */
async function handleServerInfoResource(): Promise<ReadResourceResult> {
  const content = `{{SERVER_NAME}} MCP Server

Description: {{DESCRIPTION}}
Version: {{VERSION}}
Author: {{AUTHOR}}

This server provides:
- Tools: Custom functions and commands
- Prompts: Structured prompts for AI interactions
- Resources: Dynamic content and data access

Capabilities:
- Example tool for message processing
- Example prompt for content generation
- Server information resource

For more information about MCP, visit: https://modelcontextprotocol.io/
`;

  return {
    contents: [
      {
        type: 'text',
        text: content,
      } as TextContent,
    ],
  };
}

// Add more resource handlers here
{{ADDITIONAL_RESOURCE_HANDLER_FUNCTIONS}}

/**
 * Handler for listing available tools
 */
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools };
});

/**
 * Handler for calling tools
 */
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'example_tool':
        return await handleExampleTool(args as ExampleToolArgs);

      // Add more tool handlers here
      {{ADDITIONAL_TOOL_CASES}}

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    return {
      content: [
        {
          type: 'text',
          text: `Error executing ${name}: ${errorMessage}`,
        } as TextContent,
      ],
      isError: true,
    };
  }
});

/**
 * Handler for listing available prompts
 */
server.setRequestHandler(ListPromptsRequestSchema, async () => {
  return { prompts };
});

/**
 * Handler for getting prompt content
 */
server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'example_prompt':
        return await handleExamplePrompt(args as ExamplePromptArgs);

      // Add more prompt handlers here
      {{ADDITIONAL_PROMPT_CASES}}

      default:
        throw new Error(`Unknown prompt: ${name}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    throw new Error(`Error with prompt ${name}: ${errorMessage}`);
  }
});

/**
 * Handler for listing available resources
 */
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return { resources };
});

/**
 * Handler for reading resource content
 */
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  try {
    switch (uri) {
      case '{{SERVER_NAME}}://info':
        return await handleServerInfoResource();

      // Add more resource handlers here
      {{ADDITIONAL_RESOURCE_CASES}}

      default:
        throw new Error(`Unknown resource: ${uri}`);
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    throw new Error(`Error reading resource ${uri}: ${errorMessage}`);
  }
});

/**
 * Start the server
 */
async function main(): Promise<void> {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  
  console.error('{{SERVER_NAME}} MCP Server running on stdio');
}

// Handle graceful shutdown
process.on('SIGINT', async () => {
  console.error('Shutting down {{SERVER_NAME}} MCP Server...');
  await server.close();
  process.exit(0);
});

process.on('SIGTERM', async () => {
  console.error('Shutting down {{SERVER_NAME}} MCP Server...');
  await server.close();
  process.exit(0);
});

// Start the server
main().catch((error: Error) => {
  console.error('Fatal error in {{SERVER_NAME}} MCP Server:', error);
  process.exit(1);
});