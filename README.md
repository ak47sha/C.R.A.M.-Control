# C.R.A.M. Control
> **Classwork Resource & Assessment Mapping Control**

**C.R.A.M. Control** is a lightweight Python-based task prioritization system designed for high school students navigating heavy academic schedules (8–13 subjects). Rather than relying on simple chronological sorting, the software applies a multi-variable algorithm to calculate a real-time **Priority Score** for active coursework based on deadline urgency, assignment grade weight, and estimated completion time.

---

## Key Features

* **Multi-Subject Task Log:** Manages assignments across complex academic tracks with 8 to 13 concurrent subjects.
* **Text-to-Weight Mapping:** Converts user-entered assessment types (e.g., *Periodic Test*, *Long Test*, *Homework*) into numerical priority weights without requiring manual scale inputs.
* **Composite Priority Scoring:** Automatically ranks assignments using a balanced algorithm considering urgency, grade impact, and estimated labor.
* **Real-Time Re-Sorting:** Generates a structured daily study agenda sorted from highest to lowest priority.
* **Workload Summary:** Calculates and displays total required study hours across all logged assignments to prevent burnout.

---

## Priority Scoring Logic

The program ranks coursework using a 3-pillar formula:

$$\text{Priority Score} = \text{Urgency Score} + \text{Grade Weight Score} + \text{Workload Score}$$

1. **Urgency Score (Max 100.0):**  
   Calculated exponentially as deadlines approach:
   $$\text{Urgency Score} = \left(\frac{1}{\text{Days Remaining}}\right) \times 40$$
   *(Assignments due on the current day or overdue automatically set Urgency to 100.0).*

2. **Grade Weight Score (10.0 – 50.0):**  
   Multiplies the background weight of the assessment category by 10:
   $$\text{Grade Weight Score} = \text{Assessment Weight} \times 10$$

3. **Workload Score:**  
   Factoring in labor hours so long-term projects are not delayed:
   $$\text{Workload Score} = \text{Estimated Hours} \times 2$$

---

## Assessment Hierarchy & Background Weights

The program maps user-entered task types to specific background weight values ($1.0$ to $5.0$):

| Assessment Category | Mapped Weight | Priority Impact |
| :--- | :---: | :--- |
| Periodic Test / Quarterly Exam | **5.0** | Maximum (Term-end evaluation) |
| Alternative Assessment (AA) / Major Performance Task | **4.5** | High (Capstone output / Project) |
| Major Project / Portfolio | **4.0** | High (Multi-week assignment) |
| Long Test | **3.5** | Moderate-High (Scheduled unit test) |
| Laboratory Report / Practical Exam | **3.0** | Moderate (Technical documentation) |
| Class Presentation / Group Reporting | **2.5** | Moderate (Live performance) |
| Short Quiz / Summative Quiz | **2.0** | Moderate-Low (Lesson evaluation) |
| Seatwork / In-Class Activity | **1.5** | Low (Classroom practice) |
| Recitation / Oral Participation | **1.2** | Low (Spontaneous participation) |
| Homework / Daily Assignment | **1.0** | Baseline (Standard home study) |

---

## Getting Started

### Prerequisites
* Python 3.x installed on your environment.
* Standard Python runtime (no external libraries or `pip` dependencies required).

### Installation & Execution

1. **Clone the repository:**
   ```bash
    git clone https://github.com/ak47sha/C.R.A.M-Control.git
    cd C.R.A.M-Control
