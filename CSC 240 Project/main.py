import os
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim


class MalwareDataset(Dataset):
    def init(self, data_dir, transform=None):
        self.data = []
        self.labels = []
        self.transform = transform

        for label, folder in enumerate(["benign", "malware"]):
            folder_path = os.path.join(data_dir, folder)
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    self.data.append(filepath)
                    self.labels.append(label)

    def len(self):
        return len(self.data)

    def getitem(self, idx):
        filepath = self.data[idx]
        label = self.labels[idx]

        with open(filepath, "rb") as f:
            raw_bytes = f.read()

        # Optionally truncate/pad to fixed length
        max_len = 2048  # example: only take first 2048 bytes
        byte_tensor = torch.zeros(max_len, dtype=torch.uint8)
        content = torch.tensor(list(raw_bytes[:max_len]), dtype=torch.uint8)
        byte_tensor[:len(content)] = content

        if self.transform:
            byte_tensor = self.transform(byte_tensor)

        return byte_tensor.float(), label