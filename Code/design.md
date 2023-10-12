<style>
    .level3 {
        color: #00A7BA;
    }
    .level2 {
        color: #00D37B;
    }
    .level1 {
        color: #00FF3C;
    }
    .svar {
        color: #ff5500;
    }
    .optional {
        color: #8236f5;
    }
    .argument {
        color: #ff5500;
    }
    .required {
        color: #ff0000;
    }
</style>


- [ ] <span class="level1">`!ibook`</span>
    - [ ] <span class="level2">`!ibook serve`</span>
        - Sends GVARS from the UVAR of the player to the SVAR holding allowed content
        - [ ] <span class="level3">`!book serve clear`</span>
            - Clears the books within the <span class="svar">`magic_book_settings`</svar>
            - confirm (<span class="argument">argument</span>, <span class="optional">optional</span>)
                - If this is not given, it will display a warning to the user that this will clear all the GVARs in the SVAR holding allowed content

    - [ ] <span class="level2">`!ibook sub`
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


    -  [ ] unsub <span class="level2">`!ibook unsub`
        -  book (<span class="argument">argument</span>, <span class="required">required</span>)

- [ ] <span class="level1">`!wizbook`
    - Gives overview on how to use wizbook
    - [ ] <span class="level2">`!wizbook add`
        - Provdes a help menu listing the wizard books they can add (and if they can add it)
        - [ ] <span class="level3">`!wizbook add alch`</span><span class="required">*
            - Adds Alchemical Compendium to player CVAR


        - [ ] <span class="level3">`!wizbook add required`</span><span class="required">*
            - Adds requiredomancy Archive to player CVAR


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


    - [ ] <span class="level2"> `!wizbook switch`
        - spell 1 (<span class="argument">argument</span>, <span class="required">required</span>)
        - spell 2 (<span class="argument">argument</span>, <span class="required">required</span>)


    - [ ] <span class="level2"> `!wizbook cc`


- [ ] <span class="level1"> `!primer`
    - add
    - cast
    - cc
    - remove
    - switch


