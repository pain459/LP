# suppose if we want to represent the list of numbers 12, 34, 43, 21 as a linked list.


head = {
            "value" : 12,
            "next" : {
                        "value" : 34,
                        "next" : {
                                    "value" : 43,
                                    "next" : {
                                                "value" : 21,
                                                "next" :None
                                    }
                        }
            }
}

# If we want to access the value 43.
print(head['next']['next']['value'])