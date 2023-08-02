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
static unsigned char Z_suit [52] = {};
static unsigned char Z_pattern [52] = {};
unsigned int z = 0;

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
        for (i = 0; i < 52; ++i){
                deck_order [i] = (i);
        }

        static unsigned int deal_order [52] = {};
        static unsigned int used [52] = {};
        for (i = 0; i< 52; ++i){
                used[i] = 0;
        }

        if (!Deck_shuffled) {
                // shuffle the deck
                for (i = 0; i < 52; ){
                        y = (random() % 52);
                        if (used [y] != 1){
                                deal_order [i] = deck_order[y];
                                used [y] = 1;
                                ++i;
                        }
                }
                // TBD Student code here
               Deck_shuffled = TRUE;
        }

        // Figure out the next card to give out
        // Make sure you detect when all the cards have been dealt...
        // TBD student code here

        z = 0;
        for (i = 0; i < 4; ++i){
                for (y = 0; y < 13; ++y){
                        Z_suit [z] = (i + 1);
                        Z_pattern [z] = (y + 1);
                        z++;
                }
        }
        
        static unsigned int zi = 0;
        
        if (zi < 52){
                *suit = Z_suit[deal_order[zi]];
                *pattern = Z_pattern[deal_order[zi]];
                zi++;
        } else { 
                Deck_shuffled = FALSE;
        }
} // card_get()
// end of card.c
