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

from __future__ import print_function
import sys
import time

import RPi.GPIO as GPIO

pin_datas = {
    "J721E_SK": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (29, 31, 32, 33),  # HW PWMs to skip for this test
    },
    "AM68_SK": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (32, 33, 36),  # HW PWMs to skip for this test
    },
    "AM69_SK": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (32, 33, 36),  # HW PWMs to skip for this test
    },
    "AM62_SK": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (12, 33, 35, 40),  # HW PWMs to skip for this test
    },
    "AM62A_SK": {
        "unimplemented": (7,),
        "input_only": (),
        "hw_pwm": (12, 33, 35, 36),  # HW PWMs to skip for this test
    },
    "AM62P_SK": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (24, 26, 33, 36),  # HW PWMs to skip for this test
    },
    "J722S_EVM": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (29, 31, 33),  # HW PWMs to skip for this test
    },
    "BEAGLEY-AI": {
        "unimplemented": (),
        "input_only": (),
        "hw_pwm": (32, 33),  # HW PWMs to skip for this test
    },
}

pin_data = pin_datas.get(GPIO.model)
all_pins = (
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
    29,
    31,
    32,
    33,
    35,
    36,
    37,
    38,
    40,
)

if len(sys.argv) > 1:
    all_pins = map(int, sys.argv[1:])

for pin in all_pins:
    if pin in pin_data["unimplemented"]:
        print("Pin %d unimplemented; skipping" % pin)
        continue

    if pin in pin_data["input_only"]:
        print("Pin %d input-only; skipping" % pin)
        continue

    if pin in pin_data["hw_pwm"]:
        print("Pin %d hw_pwm; skipping" % pin)
        continue

    print("Testing pin %d as OUTPUT; CTRL-C to test next pin" % pin)
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        while True:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.25)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
