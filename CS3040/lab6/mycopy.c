//---------------------------------------------------------------------
//File: mycopy.c
//
//Description:  mycopy.c opens a source file reads the information into
//              a buffer, then writes the information into a destination
//              file. 
//
//Syntax:       The command line inputs determine source and destination files
//
//Created:      9 November 2017
//              Rucker, Zaki
//---------------------------------------------------------------------

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#define VALID_ARGS 3
#define BUFSIZE 128
#define SRC_FILE argv[1]
#define DST_FILE argv[2]

FILE *Src = NULL;
FILE *Dst = NULL;

void clean (void);

void clean(void)
{
        if (Src != NULL){
                if ((fclose(Src)) != 0){
                        perror("Unable to close the source file");
                        exit(-1);
                }
                Src = NULL;
        }
        
        if (Dst != NULL){
                if ((fclose(Dst)) != 0){
                        perror("Unable to close the destination file");
                        exit(-1);
                }
                Dst = NULL;
        }
}

int main (int argc, char *argv[])
{
        char buf[BUFSIZE + 1];
        size_t num;
        unsigned int i = 0;
        unsigned int char_count = 0;
        unsigned int low_count = 0;
        unsigned int line_count = 0;
        unsigned int punct_count = 0;
        
        errno = 0;
       
        atexit(clean);

        // verify inputs
        if (argc != VALID_ARGS){
                fprintf(stderr,"Please provide 2 valid inputs, with a valid source file and destination name.\n");
                exit(-1);
        }

        if (strcmp(SRC_FILE, DST_FILE) == 0){
                fprintf(stderr,"Source and destination are the same, please choose a new destination.\n");
                exit(-1);
        }
        
        // open files
        if ((Src = fopen(SRC_FILE, "r")) == NULL){
                perror("Unable to open source file\n");
                exit(-1);
        }

        if ((Dst = fopen(DST_FILE,"r")) == NULL){
                if ((Dst = fopen(DST_FILE, "w")) == NULL){
                        perror("Unable to open destination file\n");
                        exit(-1);
                }
        } else {
                fprintf(stderr,"Dstination file already exist, try again\n");
                exit(-1);
        }
        
        // copy source file
        do {
                num = fread(buf, 1, BUFSIZE, Src);
                buf[num] = '\0';
                for (i = 0; i <= num; ++i){
                        if (buf[i] != 0){
                                ++char_count;
                                if (islower(buf[i]) != 0){
                                        ++low_count;
                                        buf[i] = toupper(buf[i]);
                                }
                                if ((buf[i]) == '\n'){
                                        ++line_count;
                                }
                                if (ispunct(buf[i]) != 0){
                                        ++punct_count;
                                }
                        }
                }
                fwrite(buf, 1, num, Dst);
        } while (!feof(Src));

        // print stats
        printf("Number of characters copied = %d\n", char_count);
        printf("Number of characters changed = %d\n", low_count);
        printf("Number of lines in the file = %d\n", line_count);
        printf("Number of punctuation chars = %d\n", punct_count);
        
        // clean house
        if (buf != NULL){
                bzero(buf, BUFSIZE + 1);
        }

        return 0;
}
