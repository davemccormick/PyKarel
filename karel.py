#!/usr/bin/env python

# Base Karel Class
class Karel(object):


    def __init__(self, position, facing, beeper_bag=0):
        ''' Constructor to setup base karel class.

            Karel is made up of its position, facing direction and beeper_bag number.

        '''

        self.__position = position
        self.__facing = facing
        self.__beeper_bag = 0

        return


    def holding_beepers(self):
        ''' Return the amount of beepers karel currently has.

        '''

        return self.__beeper_bag


    def move(self):
        ''' Sets position of karel.

        '''


        return


    def pick_beeper(self):
        ''' Increment self.__beeper_bag.

        '''

        self.__beeper_bag += 1

        return


    def put_beeper(self):
        ''' Decrement self.__beeper_bag, providing there is at least 1 beeper.

        '''

        if self.__beeper_bag > 0:
            self.__beeper_bag -= 1

        return


    def turn_left(self):
        ''' Sets direction that karel is facing.

        '''

        return
