def write(p):
    print("=" * (len(phase)+4))
    print(f"  {p}")
    print("=" * (len(phase)+4))


phase = str(input("Enter a phase: ")).strip()
write(phase)
