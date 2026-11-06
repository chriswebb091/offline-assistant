"""Offline personal assistant - chriswebb091 style.
laitos: personal assistant over satellite/SMS/chatbot,
plus web infra (DNS, proxy). This one works air-gapped:
notes live in a local JSON file, no network needed.
Usage: python persona_chris_offline_assistant.py add "buy milk"
       python persona_chris_offline_assistant.py list
       python persona_chris_offline_assistant.py search milk
"""
import json, os, sys

STORE = os.path.join(os.path.dirname(__file__), "offline_notes.json")

def load():
    return json.load(open(STORE)) if os.path.exists(STORE) else []

def save(notes):
    json.dump(notes, open(STORE, "w"), indent=2)

def main():
    if len(sys.argv) < 2:
        print("offline mode: no network needed. try: add/list/search")
        return
    cmd = sys.argv[1]
    notes = load()
    if cmd == "add":
        notes.append(" ".join(sys.argv[2:]))
        save(notes)
        print(f"saved offline: {notes[-1]}")
    elif cmd == "list":
        for i, n in enumerate(notes, 1):
            print(f"{i}. {n}")
    elif cmd == "search":
        q = " ".join(sys.argv[2:])
        for n in notes:
            if q.lower() in n.lower():
                print(n)

if __name__ == "__main__":
    main()
