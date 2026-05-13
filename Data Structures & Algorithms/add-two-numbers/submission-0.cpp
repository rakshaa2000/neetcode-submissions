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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *tail = nullptr;
        if (!l1) return l2;
        if (!l2) return l1;
        int digit = 0, carry = 0;
        while (l1 && l2){
            int sum = l1->val + l2 -> val + carry;
            digit = sum % 10;
            carry = sum / 10;
            if (!head){
                head = tail = new ListNode(digit);
            }
            else{
                tail->next = new ListNode(digit);
                tail = tail->next;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1) {
            int sum = l1->val + carry;
            digit = sum % 10;
            carry = sum / 10;
            tail->next = new ListNode(digit);
            tail = tail->next;
            l1 = l1->next;
        }
        while (l2) {
            int sum = l2->val + carry;
            digit = sum % 10;
            carry = sum / 10;
            tail->next = new ListNode(digit);
            tail = tail->next;
            l2 = l2->next;
        }
        if (carry) tail->next = new ListNode(1);
        return head;
    }
};
