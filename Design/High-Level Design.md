<link rel="stylesheet" href="styles.css">

# High-level Design

## Aliases
- [ ] <span class="level1">`!ibook`</span>
    - [ ] <span class="level2">`!ibook serve`</span>
        - Sends GVARS from the UVAR of the player to the SVAR holding allowed content
        - [ ] <span class="level3">`!book serve clear`</span>
            - Clears the books within the <span class="svar">`magic_book_settings`</svar>
            - confirm (<span class="argument">argument</span>, <span class="optional">optional</span>)
                - If this is not given, it will display a warning to the user that this will clear all the GVARs/sourcebooks in the SVAR holding allowed content


        - [ ] <span class="level3">`!book serve remove`</span>

            - Clears the books within the <span class="svar">`magic_book_settings`</svar>
            - book (<span class="argument">argument</span>, <span class="required">required</span>)
            - confirm (<span class="argument">argument</span>, <span class="optional">optional</span>)
                - If this is not given, it will display a warning to the user that this will clear all the GVARs/sourcebooks in the SVAR holding allowed content

    - [ ] <span class="level2">`!ibook sub`
        - Provides a list of the different books to subscribe to
        - [ ] <span class="level3">`!ibook sub ai`</span><span class="required">*
            - Subscribes to Acquisition's Incorporated

        - [ ] <span class="level3">`!ibook sub eepc`</span><span class="required">*
            - Subscribes to Elemental Evil Player's Companion


        - [ ] <span class="level3">`!ibook sub egtw`</span><span class="required">*
            - Subscribes to Explorers Guide to Wildemount


        - [ ] <span class="level3">`!ibook sub ftod`</span><span class="required">*
            - Subscribes to Fizban's Treasury of Dragons


        - [ ] <span class="level3">`!ibook sub ggtr`</span><span class="required">*
            - Subscribes to Guildmaster's Guide to Ravnica


        - [ ] <span class="level3">`!ibook sub idrotf`</span><span class="required">*
            - Subscribes to Icewind Dale: Rime of the Frostmaiden


        - [ ] <span class="level3">`!ibook sub llok`</span><span class="required">*
            - Subscribes to Lost Laboratory of Kwalish


        - [ ] <span class="level3">`!ibook sub phb`</span><span class="required">*
            - Subscribes to the Player's Handbook


        - [ ] <span class="level3">`!ibook sub sais`</span><span class="required">*
            - Subscribes to Spelljammer: Adventurers in Space


        - [ ] <span class="level3">`!ibook sub sacoc`</span><span class="required">*
            - Subscribes to Strixhaven: A Curriculum of Chaos


        - [ ] <span class="level3">`!ibook sub scag`</span><span class="required">*
            - Subscribes to Sword Coast Adventurer's Guide


        - [ ] <span class="level3">`!ibook sub tcsr`</span><span class="required">*
            - Subscribes to Tal'Dorei Campaign Setting Reborn


        - [ ] <span class="level3">`!ibook sub tcoe`</span><span class="required">*
            - Subscribes to Tasha's Cauldron of Everything


        - [ ] <span class="level3">`!book sub xgte`</span><span class="required">*
            - Subscribes to Xanathar's Guide to Everything


    -  [ ] <span class="level2">`!ibook unsub`
        -  Unsubscribes the user from the book in their library
        -  book (<span class="argument">argument</span>, <span class="required">required</span>)

- [ ] <span class="level1">`!wizbook`
    - Gives overview on how to use wizbook
    - [ ] <span class="level2">`!wizbook add`
        - Provdes a help menu listing the wizard books they can add (and if they can add it)
        - [ ] <span class="level3">`!wizbook add alch`</span><span class="required">*
            - Adds Alchemical Compendium to player CVAR


        - [ ] <span class="level3">`!wizbook add astr`</span><span class="required">*
            - Adds Astromancy Archive to player CVAR


        - [ ] <span class="level3">`!wizbook add atla`</span><span class="required">*
            - Adds Atlas of Endless Horizons to player CVAR


        - [ ] <span class="level3">`!wizbook add dupl`</span><span class="required">*
            - Adds Duplicious Treatise to player CVAR


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


    - [ ] <span class="level2"> `!wizbook activate`
        - book (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook cast`
        - spell (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook remove`

        - book (<span class="argument">argument</span>, <span class="required">required</span>)
        - \# (<span class="argument">argument</span>, <span class="optional">optional</span>)
  

        - [ ] <span class="level3">`!wizbook remove undo`
            - Undo removal of book


    - [ ] <span class="level2"> `!wizbook switch`
        - spell 1 (<span class="argument">argument</span>, <span class="required">required</span>)
        - spell 2 (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook cc`
        - book (<span class="argument">argument</span>, <span class="required">required</span>)
        - \# (<span class="argument">argument</span>, <span class="optional">optional</span>)

    - [ ] <span class="level2"> `!wizbook list`
        - Provides list of books (and their spell) in CVAR

- [ ] <span class="level1"> `!primer`
    - [ ] <span class="level2">`!primer add`
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
        - spell (<span class="argument">argument</span>, <span class="required">required</span>)

    - [ ] <span class="level2"> `!primer cc`
        - book (<span class="argument">argument</span>, <span class="required">required</span>)
        - \# (<span class="argument">argument</span>, <span class="optional">optional</span>)

    - [ ] <span class="level2"> `!primer remove`

        - book (<span class="argument">argument</span>, <span class="required">required</span>)
        - \# (<span class="argument">argument</span>, <span class="optional">optional</span>)

        - [ ] <span class="level3">`!primer remove undo`

            - Undo removal of book

    - [ ] <span class="level2"> `!primer switch`
        - spell 1 (<span class="argument">argument</span>, <span class="required">required</span>)
        - spell 2 (<span class="argument">argument</span>, <span class="required">required</span>)

    - [ ] <span class="level2"> `!primer list`
        - Provides list of books (and their spell) in CVAR

<span class="required">*Requires licensing

## Snippets

- [ ] <span class="level1"> `lore`
  
    - Adds a d4 to <span class="skill">`history`</span> and <span class="skill">`religion`</span> checks


- [ ] <span class="level1"> `pris`
    - Adds a d4 to <span class="skill">`acrobatics`</span> and <span class="skill">`performance`</span> checks


- [ ] <span class="level1"> `quan`
    - Adds a d4 to <span class="skill">`arcana`</span> and <span class="skill">`nature`</span> checks


- [ ] <span class="level1"> `silv`
    - Adds a d4 to <span class="skill">`intimidation`</span> and <span class="skill">`persuasion`</span> checks


- [ ] <span class="level1"> `with`
    - Adds a d4 to <span class="skill">`nature`</span> and <span class="skill">`survival`</span> checks