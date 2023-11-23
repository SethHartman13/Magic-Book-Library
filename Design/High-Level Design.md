<link rel="stylesheet" href="styles.css">

# High-level Design

## Aliases
- [x] <span class="level1">`!ibook`</span>
    - Provides help menu
    - [x] <span class="level2">`!ibook serve`</span> <span class="documented">Documented</span>
        - [Markdown](../Code/Aliases/ibook/serve/serve.md)

        - [x] <span class="level3">`!ibook serve clear`<span class="required">`[confirm/undo]`</span> <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/serve/clear/clear.md)
            
        - [x] <span class="level3">`!ibook serve remove`<span class="required">`[source/gvar/svar]`</span></span> <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/serve/remove/remove.md)

        - [x] <span class="level3">`!ibook serve add`<span class="required">`[source/gvar/svar/all]`</span></span> <span class="documented">Documented</span>

            - [Markdown](../Code/Aliases/ibook/serve/add/add.md)

        - [x] <span class="level3">`!ibook serve help`</span> <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/serve/help/help.md)

    - [x] <span class="level2">`!ibook sub` <span class="documented">Documented</span>
        - [Markdown](../Code/Aliases/ibook/sub/sub.md)
        - [x] <span class="level3">`!ibook sub ai`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/ai/ai.md)

        - [x] <span class="level3">`!ibook sub eepc`</span><span class="required">* <span class="documented">Documented</span> 
            - [Markdown](../Code/Aliases/ibook/sub/eepc/eepc.md)

        - [x] <span class="level3">`!ibook sub egtw`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/egtw/egtw.md)

        - [x] <span class="level3">`!ibook sub ftod`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/egtw/egtw.md)

        - [x] <span class="level3">`!ibook sub ggtr`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/ggtr/ggtr.md)


        - [x] <span class="level3">`!ibook sub idrotf`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/idrotf/idrotf.md)


        - [x] <span class="level3">`!ibook sub llok`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/llok/llok.md)


        - [x] <span class="level3">`!ibook sub phb`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/phb/phb.md)


        - [x] <span class="level3">`!ibook sub sais`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/sais/sais.md)


        - [x] <span class="level3">`!ibook sub sacoc`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/sacoc/sacoc.md)


        - [x] <span class="level3">`!ibook sub scag`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/scag/scag.md)


        - [x] <span class="level3">`!ibook sub tcsr`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/tcsr/tcsr.md)


        - [x] <span class="level3">`!ibook sub tcoe`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/tcoe/tcoe.md)


        - [x] <span class="level3">`!ibook sub xgte`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/ibook/sub/xgte/xgte.md)

    -  [x] <span class="level2">`!ibook unsub`<span class="required">`[source/gvar/svar]`</span></span> <span class="documented">Documented</span>
        -  [Markdown](../Code/Aliases/ibook/unsub/unsub.md)
    
    - [x] <span class="level2">`!ibook list` <span class="documented">Documented</span>
        - [Markdown](../Code/Aliases/ibook/list/list.md)

    - [x] <span class="level2">`!ibook settings`<span class="optional">`<setting_name> <setting condition>`</span></span> <span class="documented">Documented</span>
        - [Markdown](../Code/Aliases/ibook/settings/settings.md)

- [ ] <span class="level1">`!wizbook`
    - Gives overview on how to use wizbook
    - [ ] <span class="level2">`!wizbook add`
        - Provides a help menu listing the wizard books they can add (and if they can add it)
        - [ ] <span class="level3">`!wizbook add alch`</span><span class="required">*</span> <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/alch/alch.md)

        - [ ] <span class="level3">`!wizbook add astr`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/astr/astr.md)

        - [ ] <span class="level3">`!wizbook add atla`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/atla/atla.md)

        - [ ] <span class="level3">`!wizbook add crys`</span><span class="required">*</span> <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/crys/crys.md)

        - [ ] <span class="level3">`!wizbook add dupl`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/dupl/dupl.md)

        - [ ] <span class="level3">`!wizbook add fulm`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/fulm/ulm.md)

        - [ ] <span class="level3">`!wizbook add hear`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/hear/hear.md)

        - [ ] <span class="level3">`!wizbook add libr`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/libr/libr.md)

        - [ ] <span class="level3">`!wizbook add plan`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/plan/plan.md)

        - [ ] <span class="level3">`!wizbook add prot`</span><span class="required">* <span class="documented">Documented</span>
            - [Markdown](../Code/Aliases/wizbook/add/prot/prot.md)

    - [ ] <span class="level2"> `!wizbook activate`<span class="required">`[Book Name]`</span>
        - Activates the books special ability

    - [ ] <span class="level2"> `!wizbook cast`<span class="required">`[Spell Name]`</span>
        - Casts a spell from the book

    - [ ] <span class="level2"> `!wizbook remove`<span class="required">`[Book Name]`</span>
        - Removes a book from the character's CVAR

        - [ ] <span class="level3">`!wizbook remove undo`
            - Undo removal of book

    - [ ] <span class="level2"> `!wizbook switch`<span class="required">`[Magic Book Spell] [Spellbook Spell]`</span>
        - Switches out spell from their book from a spell in their spellbook

    - [ ] ~~<span class="level2"> `!wizbook cc`~~
        - Checks Custom Counter of book specified (with # modifies the counter number)
        - wizard book name (<span class="argument">argument</span>, <span class="required">required</span>)

    - [ ] <span class="level2"> `!wizbook list`
        - Provides list of wizard books (and their spells) in CVAR

- [ ] <span class="level1"> `!primer`
    - Gives help menu
    - [ ] <span class="level2">`!primer add`
        - Provides a help menu listing the primers they can add (and if they can add it)
        - [ ] <span class="level3"> `!primer add lore`</span><span class="required">*
            - Adds Lorehold Primer to player CVAR


        - [ ] <span class="level3"> `!primer add pris`</span><span class="required">*
            - Adds Prismari Primer to player CVAR


        - [ ] <span class="level3"> `!primer add quan`</span><span class="required">*
            - Adds Quandrix Primer to player CVAR


        - [ ] <span class="level3"> `!primer add silv`</span><span class="required">*
            - Adds Silverquill Primer to player CVAR


        - [ ] <span class="level3"> `!primer add with`</span><span class="required">*
            - Adds Witherbloom Primer to player CVAR

    - [ ] <span class="level2"> `!primer cast`
        - Casts spell using the primer

    - [ ] ~~<span class="level2"> `!primer cc`~~
        - primer book name (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!primer remove`<span class="required">`[Book Name]`</span>

        - [ ] <span class="level3">`!primer remove undo`</span>
            - Undo removal of book

    - [ ] <span class="level2"> `!primer switch`<span class="required">`[Primer Book Spell] [Spellbook Spell]`</span>
        - Switches spell that the primer has and switches it to the spell specified

    - [ ] <span class="level2"> `!primer list`
        - Provides list of primers (and their spell) in CVAR

## Snippets

- [ ] <span class="level1"> `lore` <span class="minor">Minor Requirement
    - Adds a d4 to <span class="skill">`history`</span> and <span class="skill">`religion`</span> checks


- [ ] <span class="level1"> `pris` <span class="minor">Minor Requirement
    - Adds a d4 to <span class="skill">`acrobatics`</span> and <span class="skill">`performance`</span> checks


- [ ] <span class="level1"> `quan` <span class="minor">Minor Requirement
    - Adds a d4 to <span class="skill">`arcana`</span> and <span class="skill">`nature`</span> checks


- [ ] <span class="level1"> `silv` <span class="minor">Minor Requirement
    - Adds a d4 to <span class="skill">`intimidation`</span> and <span class="skill">`persuasion`</span> checks


- [ ] <span class="level1"> `with` <span class="minor">Minor Requirement
    - Adds a d4 to <span class="skill">`nature`</span> and <span class="skill">`survival`</span> checks

<span class="required">*Requires licensing

<span class="rft"><strong>R</strong>eady <strong>F</strong>or <strong>T</strong>esting