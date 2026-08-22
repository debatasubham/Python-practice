import tkinter as tk
from tkinter import font
import time

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
]

BG          = "#1a1a2e"
PANEL_BG    = "#16213e"
ACCENT      = "#0f3460"
TRUE_CLR    = "#4ade80"
FALSE_CLR   = "#f87171"
TEXT_CLR    = "#e2e8f0"
SUBTEXT     = "#94a3b8"
GOLD        = "#fbbf24"
WHITE       = "#ffffff"
CORRECT_BG  = "#065f46"
WRONG_BG    = "#7f1d1d"


class QuizApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🧠 True or False Quiz")
        self.root.geometry("780x540")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.questions      = question_data[:]
        self.q_index        = 0
        self.score          = 0
        self.total          = len(self.questions)
        self.answered       = False

        self._build_ui()
        self._load_question()

    def _build_ui(self):
        # Header bar
        header = tk.Frame(self.root, bg=ACCENT, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="🧠  TRUE  OR  FALSE",
            bg=ACCENT, fg=WHITE,
            font=("Segoe UI", 18, "bold")
        ).pack(side="left", padx=24, pady=12)

        self.score_lbl = tk.Label(
            header, text="Score: 0",
            bg=ACCENT, fg=GOLD,
            font=("Segoe UI", 14, "bold")
        )
        self.score_lbl.pack(side="right", padx=24)

        self.progress_canvas = tk.Canvas(
            self.root, bg=PANEL_BG, height=8,
            highlightthickness=0
        )
        self.progress_canvas.pack(fill="x")

        self.counter_lbl = tk.Label(
            self.root, text="",
            bg=BG, fg=SUBTEXT,
            font=("Segoe UI", 10)
        )
        self.counter_lbl.pack(pady=(14, 4))

        # Question card
        card = tk.Frame(self.root, bg=PANEL_BG, bd=0)
        card.pack(fill="both", padx=48, pady=(0, 12))

        self.question_lbl = tk.Label(
            card, text="",
            bg=PANEL_BG, fg=TEXT_CLR,
            font=("Segoe UI", 14),
            wraplength=680, justify="center",
            pady=30
        )
        self.question_lbl.pack()

        # Feedback label (hidden initially)
        self.feedback_lbl = tk.Label(
            card, text="",
            bg=PANEL_BG, fg=WHITE,
            font=("Segoe UI", 12, "bold"),
            pady=6
        )
        self.feedback_lbl.pack()

        # Buttons row
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(pady=10)

        self.true_btn = self._make_button(
            btn_frame, "✓  TRUE", TRUE_CLR,
            lambda: self._check_answer("True")
        )
        self.true_btn.pack(side="left", padx=20)

        self.false_btn = self._make_button(
            btn_frame, "✗  FALSE", FALSE_CLR,
            lambda: self._check_answer("False")
        )
        self.false_btn.pack(side="left", padx=20)

        # Next button (hidden until answered)
        self.next_btn = tk.Button(
            self.root, text="Next Question  →",
            bg=ACCENT, fg=WHITE, activebackground="#1e4d8c",
            font=("Segoe UI", 11, "bold"),
            relief="flat", cursor="hand2",
            padx=24, pady=10,
            command=self._next_question
        )

    def _make_button(self, parent, text, colour, cmd):
        return tk.Button(
            parent, text=text,
            bg=colour, fg=WHITE, activebackground=colour,
            font=("Segoe UI", 13, "bold"),
            relief="flat", cursor="hand2",
            width=12, height=2,
            command=cmd
        )

    # ── Game Logic ───────────────────────────────────────────────────────────
    def _load_question(self):
        self.answered = False
        self.feedback_lbl.config(text="", bg=PANEL_BG)
        self.next_btn.pack_forget()
        self.true_btn.config(state="normal",  bg=TRUE_CLR)
        self.false_btn.config(state="normal", bg=FALSE_CLR)

        q = self.questions[self.q_index]
        self.question_lbl.config(text=q["text"])
        self.counter_lbl.config(
            text=f"Question  {self.q_index + 1}  /  {self.total}"
        )
        self._draw_progress()

    def _draw_progress(self):
        self.progress_canvas.update_idletasks()
        w = self.progress_canvas.winfo_width()
        filled = int(w * (self.q_index / self.total))
        self.progress_canvas.delete("all")
        self.progress_canvas.create_rectangle(0, 0, w, 8, fill=ACCENT, outline="")
        self.progress_canvas.create_rectangle(0, 0, filled, 8, fill=GOLD, outline="")

    def _check_answer(self, user_answer: str):
        if self.answered:
            return
        self.answered = True

        correct = self.questions[self.q_index]["answer"]
        is_correct = (user_answer == correct)

        if is_correct:
            self.score += 1
            self.score_lbl.config(text=f"Score: {self.score}")
            self.feedback_lbl.config(
                text="✅  Correct!",
                bg=CORRECT_BG, fg="#a7f3d0"
            )
        else:
            self.feedback_lbl.config(
                text=f"❌  Wrong!  The answer was  {correct}.",
                bg=WRONG_BG, fg="#fecaca"
            )

        # Dim both buttons, highlight the correct one
        correct_btn  = self.true_btn  if correct == "True"  else self.false_btn
        wrong_btn    = self.false_btn if correct == "True"  else self.true_btn
        correct_btn.config(relief="sunken")
        wrong_btn.config(state="disabled", bg="#4b5563")

        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")

        # Show next / finish button
        if self.q_index + 1 < self.total:
            self.next_btn.config(text="Next Question  →")
        else:
            self.next_btn.config(text="See Results  🏆")
        self.next_btn.pack(pady=6)

    def _next_question(self):
        self.q_index += 1
        if self.q_index < self.total:
            self._load_question()
        else:
            self._show_results()

    # ── Results Screen ───────────────────────────────────────────────────────
    def _show_results(self):
        # Clear everything
        for widget in self.root.winfo_children():
            widget.destroy()

        pct   = int(self.score / self.total * 100)
        emoji = "🏆" if pct == 100 else "🎉" if pct >= 70 else "😅" if pct >= 40 else "📚"
        msg   = (
            "Perfect score!" if pct == 100 else
            "Great job!"     if pct >= 70  else
            "Not bad!"       if pct >= 40  else
            "Keep practising!"
        )

        tk.Frame(self.root, bg=ACCENT, height=60).pack(fill="x")

        tk.Label(
            self.root, text=f"{emoji}  Quiz Complete!",
            bg=BG, fg=WHITE,
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(36, 8))

        tk.Label(
            self.root, text=msg,
            bg=BG, fg=GOLD,
            font=("Segoe UI", 14, "italic")
        ).pack()

        # Score circle (fake with a label)
        tk.Label(
            self.root,
            text=f"{self.score} / {self.total}",
            bg=PANEL_BG, fg=WHITE,
            font=("Segoe UI", 42, "bold"),
            padx=40, pady=20,
            relief="flat"
        ).pack(pady=24)

        tk.Label(
            self.root, text=f"{pct}%  correct",
            bg=BG, fg=SUBTEXT,
            font=("Segoe UI", 13)
        ).pack()

        tk.Button(
            self.root, text="🔄  Play Again",
            bg=TRUE_CLR, fg=WHITE, activebackground="#22c55e",
            font=("Segoe UI", 12, "bold"),
            relief="flat", cursor="hand2",
            padx=28, pady=10,
            command=self._restart
        ).pack(pady=28)

    def _restart(self):
        self.q_index  = 0
        self.score    = 0
        self.answered = False

        for widget in self.root.winfo_children():
            widget.destroy()

        self._build_ui()
        self._load_question()


# ── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = QuizApp(root)
    root.mainloop()
