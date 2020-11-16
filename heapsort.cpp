#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<ctime>

#define MAX 100
using namespace std;

int Arr[MAX + 1];
bool Flag[10000];

void Print()
{

    int Cnt = 0;
    for (int i = 1; i <= MAX; i++)
    {
        printf("%3d ", Arr[i]);
        Cnt++;
        if (Cnt == 20)
        {
            Cnt = 0;
            cout << endl;
        }
    }

    cout << endl;
}

void Build_Heap()
{
    for (int Cur_Idx = 2; Cur_Idx <= MAX; Cur_Idx++)
    {
        while (Cur_Idx > 1)    // if Current Idx is Not Root. Do
        {
            int Parent_Idx = Cur_Idx / 2;
            if (Arr[Cur_Idx] > Arr[Parent_Idx])
            {
                swap(Arr[Cur_Idx], Arr[Parent_Idx]);
                Cur_Idx = Parent_Idx;
            }
            else break;
        }
    }
}

void Heapify(int Current, int N)
{
    int Cur_Idx = Current;
    int Left_Child = Current * 2;
    int Right_Child = Current * 2 + 1;

    if ((Left_Child <= N) && (Arr[Left_Child] > Arr[Cur_Idx])) Cur_Idx = Left_Child;
    if ((Right_Child <= N) && (Arr[Right_Child] > Arr[Cur_Idx])) Cur_Idx = Right_Child;

    if (Cur_Idx != Current)
    {
        swap(Arr[Cur_Idx], Arr[Current]);
        Heapify(Cur_Idx, N);
    }
}

void HeapSort()
{
    Build_Heap();
    for (int i = MAX; i >= 2; i--)
    {
        swap(Arr[i], Arr[1]);
        Heapify(1, i - 1);
    }
}

int main(void)
{
    srand((unsigned)time(NULL));
    for (int i = 1; i <= MAX; )
    {
        Arr[i] = rand() % 300 + 1;
        if (Flag[Arr[i]] == false)
        {
            Flag[Arr[i]] = true;
            i++;
        }
    }

    cout << "[ Initialize Array State ]" << endl;
    Print();
    HeapSort();
    cout << "[ After Sorting Array State]" << endl;
    Print();

    return 0;
}