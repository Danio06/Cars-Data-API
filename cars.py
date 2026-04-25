cars = {
    "BMW": {
        "3_series": {

            "E21": {
                "engines": {
                    "petrol": [

                         {"model": "315", "engine": "M10B16", "power": 75},
                         {"model": "316", "engine": "M10B16/M10B18", "power": 90},
                         {"model": "318", "engine": "M10B18", "power": 90},
                         {"model": "318", "engine": "M10B18", "power": 98},
                         {"model": "318", "engine": "M10B18", "power": 106},
                         {"model": "320", "engine": "M10B20", "power": 109},
                         {"model": "320", "engine": "M20B20", "power": 122},
                         {"model": "320i", "engine": "M10B20", "power": 125},
                         {"model": "323i", "engine": "M20B23", "power": 143}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 4, "type": "Getrag 242"},
                        {"speeds": 5, "type": "Eco"},
                        {"speeds": 5, "type": "Dogleg"}
                    ],
                    "automatic": [
                        {"speeds": 3, "type": "ZF 3HP22"}
                    ]
                },
                "best_engine": {
                    "petrol": {
                        "model": "320i",
                        "engine": "M10B20",
                        "power": 125
                    }
                }
            },

            "E30": {
                "engines": {
                    "petrol": [
                        {"model": "315", "engine": "M10B16", "power": 75},
                        {"model": "316", "engine": "M10B18", "power": 90},
                        {"model": "316i", "engine": "M40B16", "power": 100},
                        {"model": "318is", "engine": "M42B18", "power": 136},
                        {"model": "320i", "engine": "M20B20", "power": 125},
                        {"model": "323i", "engine": "M20B23", "power": 150},
                        {"model": "325i", "engine": "M20B25", "power": 171}
                    ],
                    "diesel": [
                        {"model": "324d", "engine": "M21D24", "power": 86},
                        {"model": "324td", "engine": "M21D24", "power": 115}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 4, "type": "Getrag 220"},
                        {"speeds": 5, "type": "Getrag 240"},
                        {"speeds": 5, "type": "Getrag 260"},
                        {"speeds": 5, "type": "Getrag 260/5"}
                    ],
                    "automatic": [
                        {"speeds": 3, "type": "ZF 3HP22"},
                        {"speeds": 4, "type": "ZF 4HP22"},
                        {"speeds": 4, "type": "ZF 4HP22 EH"}
                    ]
                }
            },

            "E36": {
                "engines": {
                    "petrol": [
                        {"model": "316i", "engine": "M40B16", "power": 100},
                        {"model": "318is", "engine": "M42B18/M44B19", "power": 140},
                        {"model": "320i", "engine": "M50B20/M52B20", "power": 150},
                        {"model": "325i", "engine": "M50B25", "power": 192},
                        {"model": "328i", "engine": "M52B28", "power": 193}
                    ],
                    "diesel": [
                        {"model": "318tds", "engine": "M41D17", "power": 90},
                        {"model": "325tds", "engine": "M51D25", "power": 143}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 5, "type": "Getrag 220"},
                        {"speeds": 6, "type": "Getrag 226"}
                    ],
                    "automatic": [
                        {"speeds": 4, "type": "GM 4L30-E"},
                        {"speeds": 5, "type": "ZF 5HP18"}
                    ]
                }
            },

            "E46": {
                "engines": {
                    "petrol": [
                        {"model": "316i", "engine": "M43B19", "power": 105},
                        {"model": "320i", "engine": "M54B22", "power": 170},
                        {"model": "330i", "engine": "M54B30", "power": 231}
                    ],
                    "diesel": [
                        {"model": "318d", "engine": "M47D20", "power": 115},
                        {"model": "330d", "engine": "M57D30", "power": 184}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 5, "type": "Getrag 250"},
                        {"speeds": 6, "type": "ZF GS6-37BZ/DZ"}
                    ],
                    "automatic": [
                        {"speeds": 5, "type": "ZF 5HP19"}
                    ]
                }
            },

            "E90": {
                "engines": {
                    "petrol": [
                        {"model": "320i", "engine": "N46/N43", "power": 150},
                        {"model": "330i", "engine": "N52/N53", "power": 258}
                    ],
                    "diesel": [
                        {"model": "320d", "engine": "M47/N47", "power": 184},
                        {"model": "335d", "engine": "M57", "power": 286}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 6, "type": "ZF GS6"}
                    ],
                    "automatic": [
                        {"speeds": 6, "type": "ZF 6HP"}
                    ]
                }
            },

            "F30": {
                "engines": {
                    "petrol": [
                        {"model": "320i", "engine": "N20/B48", "power": 184},
                        {"model": "340i", "engine": "B58", "power": 326}
                    ],
                    "diesel": [
                        {"model": "320d", "engine": "B47", "power": 190},
                        {"model": "335d", "engine": "N57", "power": 313}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 6, "type": "Getrag/ZF"}
                    ],
                    "automatic": [
                        {"speeds": 8, "type": "ZF 8HP"}
                    ]
                }
            },

            "G20": {
                "engines": {
                    "petrol": [
                        {"model": "330i", "engine": "B48", "power": 258},
                        {"model": "M340i", "engine": "B58", "power": 374}
                    ],
                    "diesel": [
                        {"model": "320d", "engine": "B47", "power": 190},
                        {"model": "M340d", "engine": "B57", "power": 340}
                    ]
                },
                "transmission": {
                    "manual": [
                        {"speeds": 6, "type": "ZF GS6"}
                    ],
                    "automatic": [
                        {"speeds": 8, "type": "ZF 8HP"}
                    ]
                }
            }
        }
    }
}