<h2><a href="https://leetcode.com/problems/design-circular-deque/">641. Design Circular Deque</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Design your implementation of the circular double-ended queue (deque).</p>

<p style="user-select: auto;">Implement the <code style="user-select: auto;">MyCircularDeque</code> class:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">MyCircularDeque(int k)</code> Initializes the deque with a maximum size of <code style="user-select: auto;">k</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean insertFront()</code> Adds an item at the front of Deque. Returns <code style="user-select: auto;">true</code> if the operation is successful, or <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean insertLast()</code> Adds an item at the rear of Deque. Returns <code style="user-select: auto;">true</code> if the operation is successful, or <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean deleteFront()</code> Deletes an item from the front of Deque. Returns <code style="user-select: auto;">true</code> if the operation is successful, or <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean deleteLast()</code> Deletes an item from the rear of Deque. Returns <code style="user-select: auto;">true</code> if the operation is successful, or <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int getFront()</code> Returns the front item from the Deque. Returns <code style="user-select: auto;">-1</code> if the deque is empty.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">int getRear()</code> Returns the last item from Deque. Returns <code style="user-select: auto;">-1</code> if the deque is empty.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean isEmpty()</code> Returns <code style="user-select: auto;">true</code> if the deque is empty, or <code style="user-select: auto;">false</code> otherwise.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">boolean isFull()</code> Returns <code style="user-select: auto;">true</code> if the deque is full, or <code style="user-select: auto;">false</code> otherwise.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input</strong>
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong style="user-select: auto;">Output</strong>
[null, true, true, true, false, 2, true, true, true, 4]

<strong style="user-select: auto;">Explanation</strong>
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= value &lt;= 1000</code></li>
	<li style="user-select: auto;">At most <code style="user-select: auto;">2000</code> calls will be made to <code style="user-select: auto;">insertFront</code>, <code style="user-select: auto;">insertLast</code>, <code style="user-select: auto;">deleteFront</code>, <code style="user-select: auto;">deleteLast</code>, <code style="user-select: auto;">getFront</code>, <code style="user-select: auto;">getRear</code>, <code style="user-select: auto;">isEmpty</code>, <code style="user-select: auto;">isFull</code>.</li>
</ul>
</div>