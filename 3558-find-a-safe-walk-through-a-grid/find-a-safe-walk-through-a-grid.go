package main

// Point stores the coordinates for the queue
type Point struct {
	r, c int
}

func findSafeWalk(grid [][]int, health int) bool {
	m := len(grid)
	n := len(grid[0])

	// Health remaining after entering the starting cell
	startHealth := health - grid[0][0]

	if startHealth <= 0 {
		return false
	}

	// Initialize the best matrix with -1
	best := make([][]int, m)
	for i := range best {
		best[i] = make([]int, n)
		for j := range best[i] {
			best[i][j] = -1
		}
	}
	best[0][0] = startHealth

	// Standard slice-based queue with a head pointer for efficiency
	q := []Point{{0, 0}}
	head := 0

	directions := []Point{
		{1, 0}, {-1, 0}, {0, 1}, {0, -1},
	}

	for head < len(q) {
		// Popleft equivalent
		curr := q[head]
		head++
		
		r, c := curr.r, curr.c
		currentHealth := best[r][c]

		if r == m-1 && c == n-1 {
			return true
		}

		for _, dir := range directions {
			nr, nc := r+dir.r, c+dir.c

			// Bounds check
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}

			newHealth := currentHealth - grid[nr][nc]

			if newHealth <= 0 {
				continue
			}

			if newHealth > best[nr][nc] {
				best[nr][nc] = newHealth
				q = append(q, Point{nr, nc})
			}
		}
	}

	return false
}