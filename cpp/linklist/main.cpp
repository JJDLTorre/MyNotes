#include <iostream>
#include <fmt/format.h>

class Node
{
public: 
    Node(int val, Node *next): mVal{val}, mNext{next}
    {}

    int mVal;
    Node *mNext;
};


class Solution
{
public:
    static Node *insert_back(Node *head, int val) {
        Node *nextNode = new Node{val, nullptr};

        // head is empty
        if (head == nullptr) {
            return nextNode;
        }

        // Find the last node
        Node *curNode = head;
        while (curNode->mNext) {
            Node *tmp = curNode->mNext;
            curNode = tmp;
        }

        // Append the next node at the end
        curNode->mNext = nextNode;

        return head;
    }

    static void display(Node *head) {
        Node *curNode = head;
        while (curNode) {

            fmt::print("{} ", curNode->mVal);
            curNode = curNode->mNext;
        }
    }

};


int main(int, char**) 
{
    Node *head = nullptr;

    int Num = 0;
    int val = 0;
    std::cin >> Num; 
    while (Num-- > 0) {
        std::cin >> val;
        head = Solution::insert_back(head, val);
    }

    Solution::display(head);

    return 0;
}


