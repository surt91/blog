Title: Come to the dark side, our theme song is﻿ better
Date: 2011-04-05 11:22
Author: surt91
Category: archiv
Tags: Video, Tech
Slug: come-to-the-dark-side-our-theme-song-is-better
Status: published

Der Imperiale Marsch, gespielt auf einem Telefonlautsprecher von einem
AVR ATMEGA8.

<video controls="controls" height="240" type="video/webm" width="320">
<source src="vid/IM2.webm"></source>
<source src="vid/IM2.ogv"></source>
</video>

    #!C
    /*
     * ImpMarchTiny.c
     *
     * Created: 03.04.2011 21:06:57
     *  Author: surt91
     */ 
    #include <avr/io.h>  

    // Da "_delay_ms()" nur bis 261/Takt (hier 4) ms genau geht
    void long_delay(int cs) 
    {
        cs *= 1000000;
        for(; cs>0; cs--) ; // busy waiting
    }


    //This function generates the square wave that makes the piezo speaker sound at a determinated frequency.
    // dauer, Frequenz, pause danach
    void beep(unsigned int duration, unsigned int note, unsigned int pause)
    {
        //pause /= 2;
        //note -= 20;
        const int delay = (int)(10000/note);  //This is the semiperiod of each note.
        long time = (long)(duration)*20;  //This is how much time we need to spend on the note.

        while(time>0)
        {
            PORTB|=(1<<PB4);   //Set P1.2...
            long_delay(delay);
            PORTB&=~(1<<PB4);  //...then reset it...
            long_delay(delay);
            time -= delay;
        }
        long_delay(pause*50); //Add a little delay to separate the single notes
    }

    void imperialerMarsch()
    {
    beep( 350 , 392 , 100 );
    beep( 350 , 392 , 100 );
    beep( 350 , 392 , 100);
    beep( 250 , 311.1 , 100 );
    beep( 25 , 466.2 , 100 );
    beep( 350 , 392 , 100 );
    beep( 250 , 311.1 , 100);
    beep( 25 , 466.2 , 100 );
    beep( 700 , 392 , 100 );
    beep( 350 , 587.32 , 100 );
    beep( 350 , 587.32 , 100 );
    beep( 350 , 587.32 , 100 );
    beep( 250 , 622.26 , 100 );
    beep( 25 , 466.2 , 100 );
    beep( 350 , 369.99 , 100);
    beep( 250 , 311.1 , 100 );
    beep( 25 , 466.2 , 100 );
    beep( 700 , 392 , 100 );
    beep( 350 , 784 , 100 );
    beep( 250 , 392 , 100 );
    beep( 25 , 392 , 100 );
    beep( 350 , 784 , 100 );
    beep( 250 , 739.98 , 100 );
    beep( 25 , 698.46 , 100 );
    beep( 25 , 659.26 , 100 );
    beep( 25 , 622.26 , 100 );
    beep( 50 , 659.26 , 400 );
    beep( 25 , 415.3 , 200 );
    beep( 350 , 554.36 , 100);
    beep( 250 , 523.25 , 100 );
    beep( 25 , 493.88 , 100 );
    beep( 25 , 466.16 , 100 );
    beep( 25 , 440 , 100 );
    beep( 50 , 466.16 , 400);
    beep( 25 , 311.13 , 200 );
    beep( 350 , 369.99 , 100 );
    beep( 250 , 311.13 , 100 );
    beep( 25 , 392 , 100 );
    beep( 350 , 466.16 , 100 );
    beep( 250 , 392 , 100 );
    beep( 25 , 466.16 , 100);
    beep( 700 , 587.32 , 100);
    beep( 350 , 784 , 100 );
    beep( 250 , 392 , 100 );
    beep( 25 , 392 , 100 );
    beep( 350 , 784 , 100 );
    beep( 250 , 739.98 , 100);
    beep( 25 , 698.46 , 100 );
    beep( 25 , 659.26 , 100 );
    beep( 25 , 622.26 , 100 );
    beep( 50 , 659.26 , 400 );
    beep( 25 , 415.3 , 200 );
    beep( 350 , 554.36 , 100);
    beep( 250 , 523.25 , 100 );
    //beep( 25 , 493.88 , 100 );
    //beep( 25 , 466.16 , 100 );
    //beep( 25 , 440 , 100 );
    //beep( 50 , 466.16 , 400 );
    //beep( 25 , 311.13 , 200 );
    //beep( 350 , 392 , 100 );
    //beep( 250 , 311.13 , 100 );
    //beep( 25 , 466.16 , 100 );
    //beep( 300 , 392.00 , 150 );
    //beep( 250 , 311.13 , 100 );
    //beep( 25 , 466.16 , 100 );
    beep( 700 , 392, 2000);

    }


    int main(){
        DDRB=0xff;
        while(1){
            imperialerMarsch();
        }
        return 0;
    }
