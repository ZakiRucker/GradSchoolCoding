//-----------------------------------------------------------------
//File: days.c
//
//Description: days.c uses main to express a date in julian format.
//
//Syntax: 
//        inputs are given while opening the program
//        example: ./days Oct 10. 
//        main will output the julian date:
//        The number of days = 283.
//-----------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define NUM_VALID_ARGS 3
#define MIN_DAYS_MONTH 1
#define MAX_DAYS_MONTH 31
#define FEB_DAYS 28
#define SHORT_DAYS 30
#define LONG_DAYS 31
#define JAND 0
#define FEBD 31
#define MARD 59
#define APRD 90
#define MAYD 120
#define JUND 151
#define JULD 181
#define AUGD 212
#define SEPD 243
#define OCTD 273
#define NOVD 304
#define DECD 334

int date_num;
int JULIAN_DATE;
int month_num;
int days_in_month;

int main(int argc, char *argv[])
{

        //verify there are the correct number of arguments
        //print error and exit for wrong format 
        if (argc != NUM_VALID_ARGS){
                printf("Expected exactly three inputs: ./days month day\n");
                exit(-1);
        } 
        
        //verify month format
        //print error and exit for wrong format
        //change argv[1][0] to upper, if necessary
        if (strnlen((argv[1]),12) == 3){
                if (((islower(argv[1][0])) && (islower(argv[1][1])) && (islower(argv[1][2]))) ||
                        ((isupper(argv[1][0])) && (islower(argv[1][1])) && (islower(argv[1][2])))){
                        argv[1][0]=toupper(argv[1][0]);  
                } else {
                        printf("Try again with %s in the format 'Feb'\n",argv[1]);
                        exit(-1);
                } 
        } else {
                printf("%s must be 3 characters. Use format 'Mar'\n", argv[1]);
                exit(-1);
        }

        //verify date format
        //print error and exit for wrong format
        if (strlen(argv[2]) >= 3){
                printf("Date %s is too long, enter a valid date i.e. '23'.\n", argv[2]);
                exit(-1);
        }

        //verify date is only digit
        if (isdigit(argv[2][0])==0){
                printf("%s invalid date entry, try again.\n", argv[2]);
                exit(-1);
        } else if (strlen(argv[2])==2){
                if(isdigit(argv[2][1])==0){
                        printf("%s invalid date, try again.\n", argv[2]);
                        exit(-1);
                }
        }
         
        //convert argv[2] to digits        
        date_num = strtol(argv[2],NULL,10);

        //convert the month to a number
        //set variable 'month_num' to the total number of days up to the last day of the previous month.
        //set variable 'Day_of_Month' to the maximum number of days in that month. (no leap year)
        //error check: if month doesn't match print error to screen.
        //there has got to be a better way to do this
        if (strcmp(argv[1],"Jan")==0){
                        month_num = JAND;
                        days_in_month = LONG_DAYS; 
        } else if (strcmp(argv[1],"Feb")==0){
                month_num = FEBD;
                days_in_month = FEB_DAYS;
        } else if (strcmp(argv[1],"Mar")==0){
                month_num = MARD;
                days_in_month = LONG_DAYS;
        } else if (strcmp(argv[1],"Apr")==0){
                month_num = APRD;
                days_in_month = SHORT_DAYS;
        } else if (strcmp(argv[1],"May")==0){
                month_num = MAYD;
                days_in_month = LONG_DAYS;
        } else if (strcmp(argv[1],"Jun")==0){      
                month_num = JUND;
                days_in_month = SHORT_DAYS;
        } else if (strcmp(argv[1],"Jul")==0){
                month_num = JULD;
                days_in_month = LONG_DAYS;
        } else if (strcmp(argv[1],"Aug")==0){
                month_num = AUGD;
                days_in_month = LONG_DAYS;
        } else if (strcmp(argv[1],"Sep")==0){
                month_num = SEPD;
                days_in_month = SHORT_DAYS;
        } else if (strcmp(argv[1],"Oct")==0){
                month_num = OCTD;
                days_in_month = LONG_DAYS;
        } else if (strcmp(argv[1],"Nov")==0){
                month_num = NOVD;
                days_in_month = SHORT_DAYS;
        } else if (strcmp(argv[1],"Dec")==0){
                month_num = DECD;
                days_in_month = LONG_DAYS;
        } else {
                printf("%s is not a valid month\n",argv[1]);
                exit(-1);
        }

        //verify month day combo is valid (non-leap year)
        if (date_num > days_in_month){
                printf("%d is too many days for %s\n",date_num, argv[1]);
                exit(-1);
        }
        if (date_num < MIN_DAYS_MONTH){
                printf("Please enter a real date\n");
                exit(-1);
        }

        //calcute the number of days in a year
        JULIAN_DATE = (date_num + month_num);

        //print the results
        printf("The number of days = %d\n",JULIAN_DATE);

        return 0;
}
