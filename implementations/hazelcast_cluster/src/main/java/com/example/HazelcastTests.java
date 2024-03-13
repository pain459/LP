import com.hazelcast.core.Hazelcast;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IMap;
import com.hazelcast.core.IAtomicLong;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;

public class HazelcastTests {

    public static void main(String[] args) {
        // Create a Hazelcast instance
        HazelcastInstance hazelcastInstance = Hazelcast.newHazelcastInstance();

        // Perform map operations
        System.out.println("Map Operations:");
        mapOperations(hazelcastInstance);

        // Perform atomic operations
        System.out.println("\nAtomic Operations:");
        atomicOperations(hazelcastInstance);

        // Perform distributed locks
        System.out.println("\nDistributed Locks:");
        distributedLocks(hazelcastInstance);

        // Shutdown Hazelcast instance
        hazelcastInstance.shutdown();
    }

    private static void mapOperations(HazelcastInstance hazelcastInstance) {
        IMap<String, String> myMap = hazelcastInstance.getMap("my-distributed-map");

        // Put some key-value pairs into the distributed map
        myMap.put("key1", "value1");
        myMap.put("key2", "value2");
        myMap.put("key3", "value3");

        // Retrieve and print values from the map
        System.out.println("Value for key1: " + myMap.get("key1"));
        System.out.println("Value for key2: " + myMap.get("key2"));
        System.out.println("Value for key3: " + myMap.get("key3"));
    }

    private static void atomicOperations(HazelcastInstance hazelcastInstance) {
        // Increment an atomic long value
        IAtomicLong atomicLong = hazelcastInstance.getAtomicLong("my-atomic-long");
        System.out.println("Current value of atomic long: " + atomicLong.get());
        atomicLong.incrementAndGet();
        System.out.println("Incremented value of atomic long: " + atomicLong.get());
    }

    private static void distributedLocks(HazelcastInstance hazelcastInstance) {
        Lock lock = hazelcastInstance.getLock("my-distributed-lock");

        // Acquire the lock and perform some critical operations
        lock.lock();
        System.out.println("Lock acquired successfully");

        // Simulate critical section
        try {
            // Perform critical operations here
            TimeUnit.SECONDS.sleep(2);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // Release the lock when done
            lock.unlock();
            System.out.println("Lock released");
        }
    }
}
