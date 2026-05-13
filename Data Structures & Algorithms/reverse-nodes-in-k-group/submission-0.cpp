/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* prev = nullptr, *cur = head, *next = nullptr;
        int i=0;
        int size = 0;
        while (cur){
            cur = cur->next;
            size++;
        }
        if (size < k) return head;
        cur = head;
        for (i=0; i<k && cur != nullptr; i++){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        if (i < k) return head;
        if (next) head->next = reverseKGroup(next, k);
        return prev;
    }
};
