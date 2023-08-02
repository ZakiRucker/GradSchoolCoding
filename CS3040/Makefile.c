//
//  Makefile.c
//  CS3040
//
//  Created by Zaki Rucker on 10/11/17.
//  Copyright © 2017 Zaki Rucker. All rights reserved.
//

all: lines

lines: lines.c
gcc -Wall lines.c -o lines
