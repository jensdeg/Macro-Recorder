#include <iostream>
#include <windows.h>
#include <conio.h>
#include <vector>

POINT mousepos;
UINT button;

bool mouseclicked = false;
std::vector<POINT> clicks;


bool MouseClickedEvent(){
    if (GetAsyncKeyState(0x01)){
        if(!mouseclicked){
            mouseclicked = true;
            return true;
        }    
    } else {
        mouseclicked = false;
    }
    return false;
}


int main(){

    
    //mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);

    while (true)
    {
        //exits if deletes is pressed
        if(GetAsyncKeyState(0x2E)){
            for(int i = 0; i<clicks.size(); i++){
                SetCursorPos(clicks[i].x, clicks[i].y);

                std::cout << clicks[i].x << " : " << clicks[i].y << std::endl;
            }
            return EXIT_SUCCESS;
        }

        if(MouseClickedEvent()){
            GetCursorPos(&mousepos);
            clicks.push_back(mousepos);
        }
    }
    return EXIT_SUCCESS;
}




