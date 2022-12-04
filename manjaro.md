kill
    
    lsof -i
    sudo lsof -t -i tcp:8000 | xargs kill -9
    
    sudo pacman -S lsof