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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*>>> minHeap;
        for (int i=0; i<lists.size(); i++){
            if (!lists[i]) continue;
            minHeap.push({lists[i]->val, lists[i]->next});
        }
        ListNode* head = nullptr, *tail = nullptr;
        while (!minHeap.empty()){
            auto top = minHeap.top();
            minHeap.pop();
            if (!head){
                head = tail = new ListNode(top.first);
            }
            else{
                tail->next =  new ListNode(top.first);
                tail = tail->next;
            }
            if (top.second) minHeap.push({top.second->val, top.second->next});
        }
        return head;
    }
};
