#include <utility>
#include <iostream>
#include <algorithm>

void selectionSort(int *myarr, int size, bool (*comparator)(int, int));
bool ascending(int x, int y);
bool descending(int x, int y);

int main(){
    int myarr[10] = {10,4,3,6,3,8,1,2,5,7};
    selectionSort(myarr, 10, descending);
    for(int it = 0; it < 10; it++){
        std::cout<<myarr[it]<< " ";
    }

}

void selectionSort(int *myarr, int size, bool (*comparator)(int, int)){
    int smallestnum = myarr[0];
    for(int i = 0; i < size; i++){
        int smallestidx  = i;
        for(int j = i+1; j < size; j++){
            if(ascending(myarr[j],myarr[smallestidx])){
                smallestidx = j;
            }
        }
        std::swap(myarr[i], myarr[smallestidx]);
    }
}

bool ascending(int x, int y)
{
    return x < y; // swap if the first element is greater than the second
}

bool descending(int x, int y)
{
    return x > y; // swap if the first element is greater than the second
}