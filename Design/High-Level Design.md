<link rel="stylesheet" href="styles.css">

# High-level Design

## Aliases
- [ ] <span class="level1">`!ibook`</span> <span class="major">Major Requirement</span> <span class="rft">RFT</span>
    - Provides help menu
    - [ ] <span class="level2">`!ibook serve`</span> 
        - Sends GVARS from the UVAR of the player to the SVAR holding allowed content
        - [ ] <span class="level3">`!ibook serve clear`</span>
            - Clears the books within the <span class="svar">`magic_book_settings`</svar>
            - confirm (<span class="argument">argument</span>, <span class="optional">optional</span>)
                - If this is not given, it will display a warning to the user that this will clear all the GVARs/sourcebooks in the SVAR holding allowed content


        - [ ] <span class="level3">`!ibook serve remove`</span>

            - Clears a book within the <span class="svar">`magic_book_settings`</svar>
            - sourcebook name (<span class="argument">argument</span>, <span class="required">required</span>)

        - [ ] <span class="level3">`!ibook serve add`</span>

            - Adds a book within the <span class="svar">`magic_book_settings`</svar>
            - sourcebook name (<span class="argument">argument</span>, <span class="required">required</span>)

        - [ ] <span class="level3">`!ibook serve help`</span>
            - Provides help menu

    - [ ] <span class="level2">`!ibook sub`
        - Provides a list of the different sourcebooks to subscribe to
        - [x] <span class="level3">`!ibook sub ai`</span><span class="required">*
            - Subscribes to Acquisition's Incorporated

        - [x] <span class="level3">`!ibook sub eepc`</span><span class="required">*
            - Subscribes to Elemental Evil Player's Companion


        - [x] <span class="level3">`!ibook sub egtw`</span><span class="required">*
            - Subscribes to Explorers Guide to Wildemount


        - [x] <span class="level3">`!ibook sub ftod`</span><span class="required">*
            - Subscribes to Fizban's Treasury of Dragons


        - [x] <span class="level3">`!ibook sub ggtr`</span><span class="required">*
            - Subscribes to Guildmaster's Guide to Ravnica


        - [x] <span class="level3">`!ibook sub idrotf`</span><span class="required">*
            - Subscribes to Icewind Dale: Rime of the Frostmaiden


        - [x] <span class="level3">`!ibook sub llok`</span><span class="required">*
            - Subscribes to Lost Laboratory of Kwalish


        - [x] <span class="level3">`!ibook sub phb`</span><span class="required">*
            - Subscribes to the Player's Handbook


        - [x] <span class="level3">`!ibook sub sais`</span><span class="required">*
            - Subscribes to Spelljammer: Adventurers in Space


        - [x] <span class="level3">`!ibook sub sacoc`</span><span class="required">*
            - Subscribes to Strixhaven: A Curriculum of Chaos


        - [x] <span class="level3">`!ibook sub scag`</span><span class="required">*
            - Subscribes to Sword Coast Adventurer's Guide


        - [x] <span class="level3">`!ibook sub tcsr`</span><span class="required">*
            - Subscribes to Tal'Dorei Campaign Setting Reborn


        - [x] <span class="level3">`!ibook sub tcoe`</span><span class="required">*
            - Subscribes to Tasha's Cauldron of Everything


        - [x] <span class="level3">`!ibook sub xgte`</span><span class="required">*
            - Subscribes to Xanathar's Guide to Everything


    -  [ ] <span class="level2">`!ibook unsub`
        -  Unsubscribes the user from a sourcebook in their library
        -  sourcebook name (<span class="argument">argument</span>, <span class="required">required</span>)
    
    - [ ] <span class="level2">`!ibook list`
        - Lists sourcebooks the user is subscribed to

    - [ ] <span class="level2">`!ibook settings`
        - Lists the current settings
        - setting name (<span class="argument">argument</span>, <span class="optional">optional</span>)
        - setting condition (<span class="argument">argument</span>, <span class="optional">optional</span>)

- [ ] <span class="level1">`!wizbook` <span class="major">Major Requirement
    - Gives overview on how to use wizbook
    - [ ] <span class="level2">`!wizbook add`
        - Provdes a help menu listing the wizard books they can add (and if they can add it)
        - [ ] <span class="level3">`!wizbook add alch`</span><span class="required">*</span> <span class="rft">RFT</span>
            - Adds Alchemical Compendium to player CVAR

        - [ ] <span class="level3">`!wizbook add astr`</span><span class="required">*
            - Adds Astromancy Archive to player CVAR

        - [ ] <span class="level3">`!wizbook add atla`</span><span class="required">*
            - Adds Atlas of Endless Horizons to player CVAR

        - [ ] <span class="level3">`!wizbook add dupl`</span><span class="required">*
            - Adds Duplicitous Manuscript to player CVAR

        - [ ] <span class="level3">`!wizbook add fulm`</span><span class="required">*
            - Adds Fulminating Treatise to player CVAR

        - [ ] <span class="level3">`!wizbook add hear`</span><span class="required">*
            - Adds Heart Weaver's Primer to player CVAR

        - [ ] <span class="level3">`!wizbook add libr`</span><span class="required">*
            - Adds Libram of Souls and Flesh to player CVAR

        - [ ] <span class="level3">`!wizbook add plan`</span><span class="required">*
            - Adds Planecaller's Codex to player CVAR

        - [ ] <span class="level3">`!wizbook add prot`</span><span class="required">*
            - Adds Protective Verses to player CVAR

        - [ ] <span class="level3">`!wizbook add crys`</span><span class="required">*</span> <span class="minor">Minor Requirement
            - Adds Crystalline Chronicle to player CVAR


    - [ ] <span class="level2"> `!wizbook activate`
        - Activates the books special ability
        - wizard book name (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook cast`
        - Casts a spell from the book
        - spell name (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook remove`
        - Removes a book from the character's CVAR
        - wizard book name (<span class="argument">argument</span>, <span class="required">required</span>)

        - [ ] <span class="level3">`!wizbook remove undo`
            - Undo removal of book


    - [ ] <span class="level2"> `!wizbook switch`
        - Switches out spell from their book from a spell in their spellbook
        - spell name 1 (in magic book) (<span class="argument">argument</span>, <span class="required">required</span>)
        - spell name 2 (in spellbook) (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook cc`
        - Checks Custom Counter of book specified (with # modifies the counter number)
        - wizard book name (<span class="argument">argument</span>, <span class="required">required</span>)

    - [ ] <span class="level2"> `!wizbook list`
        - Provides list of wizard books (and their spells) in CVAR

- [ ] <span class="level1"> `!primer` <span class="minor">Minor Requirement
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

    - [ ] <span class="level2"> `!primer cc`
        - primer book name (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!primer remove`
        - primer book name (<span class="argument">argument</span>, <span class="required">required</span>)

        - [ ] <span class="level3">`!primer remove undo`

            - Undo removal of book

    - [ ] <span class="level2"> `!primer switch`
        - Switches spell that the primer has and switches it to the spell specified
        - spell name 1 (in magic book) (<span class="argument">argument</span>, <span class="required">required</span>)
        - spell name 2 (to be switched to) (<span class="argument">argument</span>, <span class="required">required</span>)

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