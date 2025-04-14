from datasets import Dataset

ds = Dataset.from_dict({"a": range(6)}).to_iterable_dataset(num_shards=1)
state_dict = None
# Iterate through the dataset and print examples
for idx, example in enumerate(ds):
    print(example)
    if idx == 2:
        state_dict = ds.state_dict()
        print("checkpoint")
        break
print(state_dict)