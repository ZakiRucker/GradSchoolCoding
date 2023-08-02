// ----------------------------------------------------------------------
// file: card.c
//
// Description: This file implements the CARD module. Its job is to 
//     create an interface for providing cards from a shuffled deck of
//     52 standing playing cards. Each call to card_get() will return
//     the top card in that shuffled deck. If all the cards get used, 
//     then the deck is invisibly (and unknowingly) reshuffled.
//
// Created: 2016-05-03 (P. Clark)
//
// Modifications:
// 2017-10-30 (P. Clark)
//     Added card_init().
// ----------------------------------------------------------------------
#include <stdlib.h>
#include <sys/times.h>
#include "card.h"
#include "common.h"

static unsigned int Deck_shuffled = FALSE;

// This function must be called before the first call to card_get().
extern void card_init(void)
{
        // initialize the random number generator
        srandom(times(NULL));
}

// Get a card from the current deck.
// suit: This is interpreted as follows:
//     1 = Clubs
//     2 = Hearts
//     3 = Spades
//     4 = Diamonds
// pattern: This is interpreted as the 
//     1 = Ace
//     2..10 as expected
//     11 = Jack
//     12 = Queen
//     13 = King
extern void card_get(unsigned char *suit, unsigned char *pattern)
{
        unsigned int i = 0;
        unsigned int y = 0;

        //build deck order
        unsigned int deck_order [52] = {};
        for (i = 0; i <= 52; ++i){
                deck_order [i] = (i);
        }

        unsigned int deal_order [52] = {};
        unsigned int used [52] = {};
        for (i = 0; i<= 52; ++i){
                used[i] = 0;
        }

        if (!Deck_shuffled) {
                // shuffle the deck
                for (i = 0; i < 53; ++i){
                        y = (random() % 53);
                        while (used [y] != 1){
                                deal_order [i] = deck_order[y];
                                used [y] = 1;
                        }
                }
                // TBD Student code here
               Deck_shuffled = TRUE;
        }

        // Figure out the next card to give out
        // Make sure you detect when all the cards have been dealt...
        // TBD student code here

} // card_get()
// end of card.c
