### Scrooge Coin
Here's a minified implementation of the scrooge coin system for demonstration on how the blockchain is maintained and carried.

### Repository
[https://github.com/yousseftarekkh/scroogecoin](https://github.com/yousseftarekkh/scroogecoin)

### Packages
-   [uuid](https://docs.python.org/3/library/uuid.html)
-   [Cryptography/Hazmat/Backends](https://cryptography.io/en/latest/_modules/cryptography/hazmat/backends/)
-   [Cryptography/Primitives/Hashes](https://cryptography.io/en/latest/_modules/cryptography/hazmat/primitives/hashes/)
-   [Cryptography/Primitives/Serialization](https://cryptography.io/en/latest/_modules/cryptography/hazmat/primitives/serialization/ssh/)

### Requirements
You might need to python isntall the cryprography package for all the signings that we're gonna need
`pip install cryptography` `pip install keyboard`.

Afterwards, run `python ./runner.py` and you can press `Space` key to end the simulation anytime. **Notice randomized transaction will be 0.2 seconds quick. You can edit `./runner.py` and adjust the `time.sleep(0.2)` by the value you desire.**