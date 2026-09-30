# Balloon Pop

Balloon Pop is a fast-paced 2D arcade game built with **Pygame**. Test your
reflexes by popping balloons before they fall off the screen!

---

## Features

- **Dynamic Spawning:** Balloons spawn at random sizes and fall at varying speeds.
- **Accurate Hit Detection:** Size-aware distance check (`r^2`) registers clicks reliably across the entire balloon surface.
- **Entity Variety & Scoring:**
	- **Pink (Normal):** +10 Points
	- **Yellow (Bonus):** +50 Points
	- **Red (Penalty):** -5 Points
- **Lives & Miss System:** Start with 3 lives. Letting Pink or Yellow balloons fall past the bottom costs 1 life. Red (Penalty) balloons can safely drop without costing a life.
- **Timed Round & Replayability:** 30-second round countdown. Game ends when time runs out or lives reach 0, displaying the final score banner with quick restart capabilities.

### Controls

- **Left-Click:** Pop a balloon.
- **R / SPACE:** Restart the game when the Game Over banner is displayed.

---

## Getting Started

### Prerequisites & Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install -r balloon-pop/requirements.txt
```

### Run the Game

```bash
cd balloon-pop
python main.py
```

### Folder Structure

```text
05_balloon_pop/
├── README.md
└── balloon-pop/
	├── main.py
	├── requirements.txt
	└── game/
		├── __init__.py
		├── balloon.py
		├── click_detection.py
		├── game_engine.py
		└── renderer.py
```