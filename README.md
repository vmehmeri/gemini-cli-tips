# Gemini CLI 

## Basics

To authenticate, use one of 3 options:

1. Login with Google (uses Gemini Code Assist licenses)
2. Gemini API key
3. Vertex AI

For Gemini API key, simply set the `GEMINI_API_KEY` environment variable.

To use Gemini models via Vertex AI, set these environment variables.
```
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
export GOOGLE_CLOUD_LOCATION=<LOCATION>
```


## Tip 1: Use GEMINI.md
Add project-specific context in a local GEMINI.md file.

Add general context in ~/.gemini/GEMINI.md

## Tip 2: Use MCP servers for context

**Example: Context7**

Edit the file `~/.gemini/settings.json` to add:
```
"mcpServers": {
  "context7": {
    "httpUrl": "https://mcp.context7.com/mcp",
    
  }
}
```

If the file is empty (or doesn't exist), set its contents to:
```
{
  "mcpServers": {
    "context7": {
      "httpUrl": "https://mcp.context7.com/mcp",
      
    }
  }
}
```

## Tip 3: Use custom slash commands
**Example (changelog.toml):**

This example shows how to create a robust command by defining a role for the model, explaining where to find the user's input, and specifying the expected format and behavior.

In: <project>/.gemini/commands/changelog.toml
```
description = "Adds a new entry to the project's CHANGELOG.md file."
prompt = """
# Task: Update Changelog

You are an expert maintainer of this software project. A user has invoked a command to add a new entry to the changelog.

**The user's raw command is appended below your instructions.**

Your task is to parse the `<version>`, `<change_type>`, and `<message>` from their input and use the `write_file` tool to correctly update the `CHANGELOG.md` file.

## Expected Format
The command follows this format: `/changelog <version> <type> <message>`
- `<type>` must be one of: "added", "changed", "fixed", "removed".

## Behavior
1. Read the `CHANGELOG.md` file.
2. Find the section for the specified `<version>`.
3. Add the `<message>` under the correct `<type>` heading.
4. If the version or type section doesn't exist, create it.
5. Adhere strictly to the "Keep a Changelog" format.
"""
```


Now, when you run `/changelog 1.2.0 added "New feature"`, the final text sent to the model will be the original prompt followed by two newlines and the command you typed.


## Tip 4: Use /memory as a shortcut to add info in GEMINI.md
For example, in the middle of a session:

```
/memory add Always create RESTful API endpoints when adding new API routes
```

## Tip 5: Use checkpointing
The Gemini CLI includes a Checkpointing feature that automatically saves a snapshot of your project's state before any file modifications are made by AI-powered tools

When you approve a tool that modifies the file system (like write_file or replace), the CLI automatically creates a "checkpoint." This checkpoint includes:

1. A Git Snapshot: A commit is made in a special, shadow Git repository located in your home directory (~/.gemini/history/<project_hash>). This snapshot captures the complete state of your project files at that moment. It does not interfere with your own project's Git repository.
2. Conversation History: The entire conversation you've had with the agent up to that point is saved.
3. The Tool Call: The specific tool call that was about to be executed is also stored.

## Tip 6: Headless mode 
Gemini CLI can also work in headless mode. Great for automation or background tasks:

```
gemini -p "Create a commit message"
```

## Tip 7: Save/resume Chat sessions 
While chat histories are kept automatically, you can save conversations with a given name for easier retrieval (and/or longer retention):

```
/chat save mytag1
/chat list
/chat resume mytag1
/chat delete mytag1
```

Very useful for long debugging sessions or when you want to “park” a conversation until later.

## Tip 8: Multi-directory mode
You have gemini work with multiple directories by starting with the `--include-directories` option:

```
gemini --include-directories backend frontend
```

## Tip 9: Use @path/to/file for includes 
During a session, you can type the @ symbol and start typing the name of the file you want to refer to. The CLI will automatically display matching files

## Tip 10: Use /compress to reduce context 
If you wrapped up an implementation part and want to move on to another but still keep a high-level summary of what was done, the `/compress` command is ideal for this.

Context compression will run automatically when the context is exhausted. But you can trigger your own compressions strategically, to prevent "context rot"

## Bonus tip: use Google Search
Gemini CLI can use Google Search natively. Ask it, for example, for update to date documentation and code samples:

```
Search Google ADK documentation and show me some code samples from there
```

