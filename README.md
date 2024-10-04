# Poker Analyzer

## Setup Instructions

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv outspeed_env
   source outspeed_env/bin/activate
   ```

2. Upgrade pip:

   ```bash
   pip install --upgrade pip
   ```

3. Install Outspeed with Silero:

   ```bash
   pip install "outspeed[silero]"
   ```

4. Verify Outspeed installation:
   ```bash
   pip list | grep outspeed
   ```
   Expected output:
   ```
   outspeed                       0.1.136
   ```

## Current Issues

Attempting to import `realtime` module fails:

```
(outspeed_env) (base) jamesinseidel@COV-JS-MBP poker-analyzer % python
Python 3.9.12 (main, Apr  5 2022, 01:53:17)
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import realtime
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'realtime'
>>> from outspeed import realtime
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'realtime' from 'outspeed' (/Users/jamesinseidel/Documents/chapter-one-dev/poker-analyzer/outspeed_env/lib/python3.9/site-packages/outspeed/__init__.py)
```
