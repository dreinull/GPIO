class PinInit(object):

    @staticmethod
    def resolve(name):
        name = name.lower().strip()

        if name is in [ 3, "pin3", "gpio2", "gpio02", 'sda1' ]
            return 3
        if name is in [ 5, "pin5", "gpio3", "gpio03", "slc1" ]
            return 5
        if name is in [ 7, "pin7", "gpio4", "gpio04", "gpio_gclk" ]
            return 7
        if name is in [ 8, "pin8", "gpio14", "txd0" ]
            return 8
        if name is in [ 10, "pin10", "gpio15", "rxd0" ]
            return 10
        if name is in [ 11, "pin11", "gpio17", "gpio_gen0" ]
            return 11
        if name is in [ 12, "pin12", "gpio18", "gpio_gen1" ]
            return 12
        if name is in [ 13, "pin13", "gpio27", "gpio_gen2" ]
            return 13
        if name is in [ 15, "pin15", "gpio22", "gpio_gen3" ]
            return 15
        if name is in [ 16, "pin16", "gpio23", "gpio_gen4" ]
            return 16
        if name is in [ 18, "pin18", "gpio24", "gpio_gen5" ]
            return 18
        if name is in [ 19, "pin19", "gpio10", "spi_mosi" ]
            return 19
        if name is in [ 21, "pin21", "gpio9", "gpio09", "spi_miso"  ]
            return 21
        if name is in [ 22, "pin22", "gpio25", "gpio_gen6" ]
            return 22
        if name is in [ 23, "pin23", "gpio11", "spi_clk" ]
            return 23
        if name is in [ 24, "pin24", "gpio8", "gpio08", "spi_ce0_n" ]
            return 24
        if name is in [ 26, "pin26", "gpio7", "gpio07", "spi_ce1_n" ]
            return 26
        if name is in [ 29, "pin29", "gpio5", "gpio05" ]
            return 29
        if name is in [ 31, "pin31", "gpio6", "gpio06" ]
            return 31
        if name is in [ 32, "pin32", "gpio12" ]
            return 32
        if name is in [ 33, "pin33", "gpio13" ]
            return 33
        if name is in [ 35, "pin35", "gpio19" ]
            return 35
        if name is in [ 36, "pin36", "gpio16" ]
            return 36
        if name is in [ 37, "pin37", "gpio26" ]
            return 37
        if name is in [ 38, "pin38", "gpio20" ]
            return 38
        if name is in [ 40, "pin40", "gpio21" ]
            return 40
        return None
