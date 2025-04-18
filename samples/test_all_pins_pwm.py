#!/usr/bin/env python3

# Copyright (c) 2019-2020, NVIDIA CORPORATION. All rights reserved.
# Copyright (c) 2021-2023, Texas Instruments Incorporated. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import RPi.GPIO as GPIO
import time

all_pwm_pins = {
    "J721E_SK": {
        "sw_pwm": [11, 12, 15, 16],  # Can be any valid GPIO pins
        "hw_pwm": [29, 31, 32, 33],  # Designated HW PWM pins
    },
    "AM68_SK": {
        "sw_pwm": [7, 15, 19, 21, 22, 23, 24, 26, 29, 31],  # Can be any valid GPIO pins
        "hw_pwm": [32, 33, 36],  # Designated HW PWM pins
    },
    "AM69_SK": {
        "sw_pwm": [7, 15, 19, 21, 22, 23, 24, 26, 29, 31],  # Can be any valid GPIO pins
        "hw_pwm": [32, 33, 36],  # Designated HW PWM pins
    },
    "AM62_SK": {
        "sw_pwm": [
            14,
            33,
            36,
            38,
            39,
            40,
            41,
            42,
        ],  # Can be any valid GPIO pins
        "hw_pwm": [12, 33, 36, 40],  # Designated HW PWM pins
    },
    "AM62A_SK": {
        "sw_pwm": [
            8,
            10,
            11,
            12,
            13,
            15,
            16,
            18,
            19,
            21,
            22,
            23,
            24,
            26,
            29,
            31,
            32,
            37,
            38,
            40,
        ],  # Can be any valid GPIO pins
        "hw_pwm": [12, 33, 35, 36],  # Designated HW PWM pins
    },
    "AM62P_SK": {
        "sw_pwm": [
            8,
            10,
            11,
            13,
            15,
            16,
            18,
            19,
            21,
            22,
            23,
            29,
            31,
            32,
            37,
        ],  # Can be any valid GPIO pins
        "hw_pwm": [24, 26, 33, 36],  # Designated HW PWM pins
    },
    "J722S_EVM": {
        "sw_pwm": [
            7,
            8,
            10,
            11,
            12,
            13,
            15,
            16,
            18,
            19,
            21,
            22,
            23,
            24,
            26,
            32,
            35,
            37,
            38,
            40,
        ],  # Can be any valid GPIO pins
        "hw_pwm": [29, 31, 33],  # Designated HW PWM pins
    },
    "BEAGLEY-AI": {
        "sw_pwm": [
            8,
        ],  # Can be any valid GPIO pins
        "hw_pwm": [32, 33],  # Designated HW PWM pins
    },
}

pin_data = all_pwm_pins.get(GPIO.model)

pwm_pins = pin_data["sw_pwm"] + pin_data["hw_pwm"]


def main():
    for pin in pwm_pins:
        print("Testing pin %d as PWM" % pin)

        # Board pin-numbering scheme
        GPIO.setmode(GPIO.BOARD)

        # set pin as an output pin with optional initial state of HIGH
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        p = GPIO.PWM(pin, 50)
        val = 25
        incr = 5
        p.start(val)

        try:
            cnt = 0
            while cnt < 10:
                cnt += 1
                time.sleep(0.25)
                if val >= 100:
                    incr = -incr
                if val <= 0:
                    incr = -incr
                val += incr
                p.ChangeDutyCycle(val)
        except KeyboardInterrupt:
            pass
        finally:
            pass

        p.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
