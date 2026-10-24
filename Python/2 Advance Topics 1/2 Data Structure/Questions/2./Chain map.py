from collections import ChainMap as cm 

def main () -> None :
    #raise ValueError('main not implemented')

    config1 = {"debug": True, "theme": "dark"}
    config2 = {"theme": "light", "version": 2.0}
    config3 = {"version": 3.0, "autosave": True}

    combined_config = cm(config1, config2, config3)
    print(list(combined_config.keys()))
    
    key = input('Enter a key from the aboce that you want to see: ')
    print(combined_config.get(key))


    key = input('Enter a key from the aboce that you want to change: ')
    val = input('Enter the change: ')
    combined_config[key] = val
    print(combined_config.get(key))
    print(config1)


    return

if __name__ == "__main__" :
    main()