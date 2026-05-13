class LRUCache {
public:
    int size;
    list<int> order;
    unordered_map<int, pair<list<int>::iterator, int>> cache;
    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {
        if (!cache.count(key)) return -1;
        order.erase(cache[key].first);
        order.push_back(key);
        return cache[key].second;
    }
    
    void put(int key, int value) {
        if (cache.count(key)){
            order.erase(cache[key].first);
        }
        else if (cache.size() == size){
            int lru = order.front();
            order.pop_front();
            cache.erase(lru);
        }
        order.push_back(key);
        cache[key].second = value;
        cache[key].first = --order.end();
    }
};
