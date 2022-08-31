#include <iostream>
#include <thread>
using namespace std;

// A dummy function
void foo(int Z)
{
    for (int i = 0; i < Z; i++) {
        cout << "Thread using function"
               " pointer as callable\n";
    }
}

 class thread_obj {
    public:
        void operator()(int x){
            for(int i = 0; i < x; i++){
                cout << "Thread using function"
                  " object as  callable\n";
            }
        }

 } ;

 int main(){
    std::cout << "THREADS 1 and 2 and 3 are operating indepedently";

    thread th1(foo, 3);
    thread th2(thread_obj(), 3);

    auto f = [](int x){
        for (int i = 0; i < x; i++)
            cout << "Thread using lambda"
             " expression as callable\n";
    };

    thread th3(f, 3);

    th1.join();
  
    // Wait for thread t2 to finish
    th2.join();
  
    // Wait for thread t3 to finish
    th3.join();
    return 0;
 }