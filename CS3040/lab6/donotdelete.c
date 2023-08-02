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

int main (int argc, char *argv[])
{
        FILE *src = NULL;
        FILE *dst = NULL;
        char buf[BUFSIZE + 1];
        size_t num;
        unsigned int i = 0;
        unsigned int char_count = 0;
        unsigned int low_count = 0;
        unsigned int line_count = 0;
        unsigned int punct_count = 0;
        
        errno = 0;
        
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
        if ((src = fopen(SRC_FILE, "r")) == NULL){
                perror("Unable to open source file\n");
                exit(-1);
        }

        if ((dst = fopen(DST_FILE,"r")) == NULL){
                if (dst != NULL){
                        fclose(dst);
                }
                if ((dst = fopen(DST_FILE, "w")) == NULL){
                        perror("Unable to open destination file\n");
                        if (fclose(src) != 0){
                                perror("Unable to close source file\n");
                        }
                        exit(-1);
                }
        } else {
                fprintf(stderr,"dstination file already exist, try again\n");
                if (fclose(src) != 0){
                        perror("Unable to close source file\n");
                }
                if (fclose(dst) != 0){
                        perror("Unable to close destination file\n");
                }
                exit(-1);
        }
        
        // copy source file
        do {
                num = fread(buf, 1, BUFSIZE, src);
                buf[num] = '\0';
                for (i = 0; i <= num; ++i){
                        if (buf[i] != 0){
                                if (isascii(buf[i]) != 0){
                                        ++char_count;
                                }
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
                fwrite(buf, 1, num, dst);
        } while (!feof(src));

        // print stats
        printf("Number of characters copied = %d\n", char_count);
        printf("Number of characters changed = %d\n", low_count);
        printf("Number of lines in the file = %d\n", line_count);
        printf("Number of punctuation chars = %d\n", punct_count);
        
        // clean house
        if (buf != NULL){
                bzero(buf, BUFSIZE + 1);
        }

        if (src != NULL){
                if ((fclose(src)) != 0){
                        perror("Unable to close the source file");
                        exit(-1);
                }
                src = NULL;
        }
        
        if (dst != NULL){
                if ((fclose(dst)) != 0){
                        perror("Unable to close the destination file");
                        exit(-1);
                }
                dst = NULL;
        }

        return 0;
}
