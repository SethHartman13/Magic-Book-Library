<h1><i>ibook serve</i> <u>clear</u><img align="right" src="../../../../Images/image.png" width="100px"></h1>

Subalias that clears the served content within the `ibook_settings` server variable.

## Help:
`!ibook serve clear [confirm/undo]`: Requires permissions to edit server variables. Either [Administrator](https://discord.com/community/permissions-on-discord-discord#:~:text=The%20Administrator%20permission%20is%20a,on%20an%20as%2Dneeded%20basis.) Discord permissions or a role named "Server Aliaser" or "Dragonspeaker" is required.

`[confirm/undo]` is a required argument:
- `confirm`: Confirms clearing of the sourcebooks that have already been served.
- `undo`: Pulls last instance from backup and restores the clearing.

If `confirm` is not given when clearing, it will return an error.