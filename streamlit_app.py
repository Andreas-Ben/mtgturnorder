import streamlit as st

st.title("An Interactive Guide for MTG Turn Order")

st.write('Disclaimer: "Benée’s MTGTURNORDER" is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. Portions of the materials used are property of Wizards of the Coast. ©Wizards of the Coast LLC.')
st.write("To see more info on a step or phase you can click on it to expand it")

with st.expander("**501. Beginning Phase**", expanded=True):
    with st.expander("**502. Untap Step**"):
        st.write("**You untap all your tapped permanents. On the first turn of the game, you don’t have any permanents, so you just skip this step. No one can cast spells or activate abilities during this step**")
        with st.expander("Phasing happens"):
            st.write("502.1. First, all phased-in permanents with phasing that the active player controls phase out, and all phased-out permanents that the active player controlled when they phased out phase in. This all happens simultaneously. This turn-based action doesn’t use the stack. See rule 702.25, “Phasing.”")
        with st.expander("Untap all permanents"):
            st.write("502.2. Second, the active player determines which permanents they control will untap. Then they untap them all simultaneously. This turn-based action doesn’t use the stack. Normally, all of a player’s permanents untap, but effects can keep one or more of a player’s permanents from untapping.")
        with st.expander("No Priority doing untap step"):
                st.write("502.3. No player receives priority during the untap step, so no spells can be cast or resolve and no abilities can be activated or resolve. Any ability that triggers during this step will be held until the next time a player would receive priority, which is usually during the upkeep step. (See rule 503, “Upkeep Step.”)")
    with st.expander("**503. Upkeep Step**"):
        st.write('**Players can cast instants and activate abilities. This part of the turn is mentioned on a number of cards. If something is supposed to happen just once per turn, right at the beginning, an ability will trigger "at the beginning of your upkeep."**')
        with st.expander("Trigger abilities"):
            st.write("503.1a Any abilities that triggered during the untap step and any abilities that triggered at the beginning of the upkeep are put onto the stack before the active player gets priority; the order in which they triggered doesn’t matter. (See rule 603, “Handling Triggered Abilities.”)")
        with st.expander("Player Gets Priority"):
            st.write("503.1. The upkeep step has no turn-based actions. Once it begins, the active player gets priority. (See rule 116, “Timing and Priority.”)")
        #st.write("")
    with st.expander("**504. Draw Step**"):
        st.write("**You must draw a card from your library (even if you don’t want to). The player who goes first in a two-player game skips the draw step on their first turn to make up for the advantage of going first. Players can then cast instants and activate abilities.**")
        with st.expander("Draw a Card"):
            st.write("504.1. First, the active player draws a card. This turn-based action doesn’t use the stack.")
        with st.expander("Player gets priority"):  
            st.write("504.2. Second, the active player gets priority. (See rule 116, “Timing and Priority.”)")
        #st.write("")

with st.expander("**505.1 Precombat Mainphase**"):
    st.write("**You can cast any number of sorceries, instants, creatures, artifacts, enchantments, and planeswalkers, and you can activate abilities. You can play a land during this phase, but remember that you can play only one land during your turn. Your opponent can cast instants and activate abilities.**")
    with st.expander("Put lore counters on Saga enchantments"):
        st.write("505.4. If the active player controls one or more Saga enchantments and it’s the active player’s precombat main phase, the active player puts a lore counter on each Saga they control. (See rule 714, “Saga Cards.”) This turn-based action doesn’t use the stack.")
    with st.expander("Player gets priority"):
        st.write("505.5. The active player gets priority. (See rule 116, “Timing and Priority.”)")

with st.expander("**506. Combat Phase**", expanded=True):
    with st.expander("**507. Beginning of Combat Step**"):
        st.write("Players can cast instants and activate abilities.")
        with st.expander("Choose defending player"):
            st.write("507.1. First, if the game being played is a multiplayer game in which the active player’s opponents don’t all automatically become defending players, the active player chooses one of their opponents. That player becomes the defending player. This turn-based action doesn’t use the stack. (See rule 506.2.)")
        with st.expander("Player gets priority"):
            st.write("507.2. Second, the active player gets priority. (See rule 116, “Timing and Priority.”)")
    with st.expander("**508. Declare Attackers Step**"):
        st.write("You decide which, if any, of your untapped creatures will attack, and which player or planeswalker they will attack. This taps the attacking creatures. Players can then cast instants and activate abilities.")
        with st.expander("Declare untapped Attackers"):
            st.write("508.1. First, the active player declares attackers. This turn-based action doesn’t use the stack. [...]")
            st.write("508.1a The active player chooses which creatures that they control, if any, will attack. The chosen creatures must be untapped, and each one must either have haste or have been controlled by the active player continuously since the turn began.")
        with st.expander("Trigger abilities"):
            st.write("508.2a Abilities that trigger on a creature attacking trigger only at the point the creature is declared as an attacker.")
            st.write("508.2b Any abilities that triggered on attackers being declared or that triggered during the process described in rules 508.1 are put onto the stack before the active player gets priority;")
        with st.expander("Player gets priority"):
            st.write("508.2. Second, the active player gets priority. (See rule 116, “Timing and Priority.”)")
        with st.expander("It's too late to tap attackers by now"):
            st.write("506.4b Tapping or untapping a creature that’s already been declared as an attacker or blocker doesn’t remove it from combat and doesn’t prevent its combat damage.")
    with st.expander("**509. Declare Blockers Step**"):
        st.write("Your opponent decides which, if any, of their untapped creatures will block your attacking creatures. If multiple creatures block a single attacker, you order the blockers to show which will be first to receive damage, which will be second, and so on. Players can then cast instants and activate abilities.")
        with st.expander("Declare Blockers"):
            st.write("509.1. First, the defending player declares blockers. This turn-based action doesn’t use the stack. [...]")
        with st.expander("Attacker Chooses blocking order for creatures blocked by multiple blockers"):
            st.write("509.2. Second, for each attacking creature that’s become blocked, the active player announces that creature’s damage assignment order, which consists of the creatures blocking it in an order of that player’s choice.")
        with st.expander("Defending Player chooses the order of dealing damage for one creature blocking multiple attackers (e.g. Avatar of Hope)"):
            st.write("509.3. Third, for each blocking creature, the defending player announces that creature’s damage assignment order, which consists of the creatures it’s blocking in an order of that player’s choice. (During the combat damage step, a blocking creature can’t assign combat damage to a creature it’s blocking unless each creature ahead of that blocked creature in its order is assigned lethal damage.) This turn-based action doesn’t use the stack.")
        with st.expander("Trigger abilities"):
            st.write("	509.4a Any abilities that triggered on blockers being declared or that triggered during the process described in rules 509.1–3 are put onto the stack before the active player gets priority; the order in which they triggered doesn’t matter. (See rule 603, “Handling Triggered Abilities.”)")
        with st.expander("Player gets priority"):
            st.write("509.4. Fourth, the active player gets priority. (See rule 116, “Timing and Priority.”)")
    with st.expander("**510. Combat Damage Step**"):
        st.write("Each attacking or blocking creature that’s still on the battlefield assigns its combat damage to the defending player (if it’s attacking that player and wasn’t blocked), to a planeswalker (if it’s attacking that planeswalker and wasn’t blocked), to the creature or creatures blocking it, or to the creature it’s blocking. If an attacking creature is blocked by multiple creatures, you divide its combat damage among them by assigning at least enough damage to the first blocking creature to destroy it, then by assigning damage to the second one, and so on. Once players decide how the creatures they control will deal their combat damage, the damage is all dealt at the same time. Players can then cast instants and activate abilities.")
        with st.expander("Players announce how creatures deal damage"):
            st.write("510.1. First, the active player announces how each attacking creature assigns its combat damage, then the defending player announces how each blocking creature assigns its combat damage. This turn-based action doesn’t use the stack. A player assigns a creature’s combat damage according to the following rules:")
            st.write("510.1a Each attacking creature and each blocking creature assigns combat damage equal to its power. Creatures that would assign 0 or less damage this way don’t assign combat damage at all.")
            st.write("510.1b An unblocked creature assigns its combat damage to the player or planeswalker it’s attacking. If it isn’t currently attacking anything (if, for example, it was attacking a planeswalker that has left the battlefield), it assigns no combat damage.")
            st.write("510.1c A blocked creature assigns its combat damage to the creatures blocking it. If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage. If exactly one creature is blocking it, it assigns all its combat damage to that creature. If two or more creatures are blocking it, it assigns its combat damage to those creatures according to the damage assignment order announced for it.")
            st.write("510.1d A blocking creature assigns combat damage to the creatures it’s blocking. If it isn’t currently blocking any creatures (if, for example, they were destroyed or removed from combat), it assigns no combat damage. If it’s blocking exactly one creature, it assigns all its combat damage to that creature. If it’s blocking two or more creatures, it assigns its combat damage to those creatures according to the damage assignment order announced for it. [..]")
        with st.expander("Damage is dealt"):
            st.write("510.2. Second, all combat damage that’s been assigned is dealt simultaneously. This turn-based action doesn’t use the stack. No player has the chance to cast spells or activate abilities between the time combat damage is assigned and the time it’s dealt.")
        with st.expander("Trigger abilities"):
            st.write("510.3a Any abilities that triggered on damage being dealt or while state-based actions are performed afterward are put onto the stack before the active player gets priority; the order in which they triggered doesn’t matter. (See rule 603, “Handling Triggered Abilities.”)")
        with st.expander("Player gets priority"):
            st.write("510.3. Third, the active player gets priority. (See rule 116, “Timing and Priority.”)")
    with st.expander("**511. End of Combat Step**"):
        st.write("Players can cast instants and activate abilities.")
        with st.expander("Trigger abilities"):
            st.write("511.2. Abilities that trigger “at end of combat” trigger as the end of combat step begins. Effects that last “until end of combat” expire at the end of the combat phase.")
        with st.expander("Player gets priority"):
            st.write("	511.1. The end of combat step has no turn-based actions. Once it begins, the active player gets priority. (See rule 116, “Timing and Priority.”)")
with st.expander("**505.1 Postcombat Mainphase**"):
    st.write("**You can cast any number of sorceries, instants, creatures, artifacts, enchantments, and planeswalkers, and you can activate abilities. You can play a land during this phase, but remember that you can play only one land during your turn. Your opponent can cast instants and activate abilities.**")
    with st.expander("Player gets priority"):
        st.write("505.5. The active player gets priority. (See rule 116, “Timing and Priority.”)")
with st.expander("**512. Ending Phase**", expanded=True):
    with st.expander("513. End Step"):
        st.write(" Step	Abilities that trigger “at the beginning of your end step” go on the stack. Players can cast instants and activate abilities.")
        with st.expander("Trigger abilities"):
            st.write("513.1a Previously, abilities that triggered at the beginning of the end step were printed with the trigger condition “at end of turn.” Cards that were printed with that text have received errata in the Oracle card reference to say “at the beginning of the end step” or “at the beginning of the next end step.”")
        with st.expander("Player gets priority"):
            st.write("513.1. The end step has no turn-based actions. Once it begins, the active player gets priority. (See rule 116, “Timing and Priority.”)")
    with st.expander("514. Cleanup Step"):
        st.write("If you have more than seven cards in your hand, choose and discard cards until you have only seven. Next, all damage on creatures is removed and all “until end of turn” effects end. No one can cast instants or activate abilities unless an ability triggers during this step.")
        with st.expander("Discard to match max. handsize"):
            st.write("514.1. First, if the active player’s hand contains more cards than their maximum hand size (normally seven), they discard enough cards to reduce their hand size to that number. This turn-based action doesn’t use the stack.")
        with st.expander("Trigger abilities"):
            st.write("514.3a At this point, the game checks to see if any state-based actions would be performed and/or any triggered abilities are waiting to be put onto the stack (including those that trigger “at the beginning of the next cleanup step”). If so, those state-based actions are performed, then those triggered abilities are put on the stack, then the active player gets priority. Players may cast spells and activate abilities. Once the stack is empty and all players pass in succession, another cleanup step begins.")
        with st.expander("Only if abilities have triggered: Player gets priority"):
            st.write("514.3. Normally, no player receives priority during the cleanup step, so no spells can be cast and no abilities can be activated. However, this rule is subject to the following exception:")
