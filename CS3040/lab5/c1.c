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
// 2017-11-3 (Z. Rucker)
//      provided program to card_get().
// ----------------------------------------------------------------------
#include <stdlib.h>
#include <sys/times.h>
#include "card.h"
#include "common.h"

#define FULL_DECK 52
#define FULL_SUIT 13
#define ALL_SUITS 4

static unsigned int Deck_shuffled = FALSE;

// This function must be called before the first call to card_get().
extern void card_init(void)
{
        // initialize the random number generator
        srandom(times(NULL));
}

extern void card_get(unsigned char *suit, unsigned char *pattern)
{
        unsigned int i = 0;
        unsigned int y = 0;
        unsigned int deck_order [FULL_DECK] = {};
        static unsigned int deal_order [FULL_DECK] = {};
        static unsigned int used [FULL_DECK] = {};
        static unsigned int card_counter = 0;

        //build fresh deck order
        //for (i = 0; i < FULL_DECK; ++i){
        //}

        if (!Deck_shuffled) {
                for (i = 0; i < FULL_DECK; ++i){
                        deck_order [i] = (i);
                        used[i] = 0;
                }
                // shuffle the deck
                for (i = 0; i < FULL_DECK; ){
                        y = (random() % FULL_DECK);
                        if (used [y] != 1){
                                deal_order [i] = deck_order[y];
                                used [y] = 1;
                                ++i;
                        }
                }
               Deck_shuffled = TRUE;
        }
        // Figure out the next card to give out
        if (card_counter < FULL_DECK){
                *suit = ((deal_order[card_counter])/FULL_SUIT + 1);
                *pattern = ((deal_order[card_counter])%FULL_SUIT + 1);
                card_counter++;
        } else { 
                Deck_shuffled = FALSE;
        }
} // card_get()
// end of card.c
