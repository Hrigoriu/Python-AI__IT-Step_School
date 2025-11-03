import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)  # вхідний шар
        self.fc2 = nn.Linear(128, 64)     # прихований шар
        self.fc3 = nn.Linear(64, 10)      # вихідний шар (10 класів)

    def forward(self, x):
        x = x.view(-1, 28*28)             # розгортаємо зображення в вектор
        x = F.relu(self.fc1(x))           # активація ReLU
        x = F.relu(self.fc2(x))
        x = self.fc3(x)                   # без softmax — буде втрата cross-entropy
        return x

transform = transforms.ToTensor()

train_data = datasets.MNIST(root='mnist_data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

model = SimpleNN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(5):
    for images, labels in train_loader:
        optimizer.zero_grad()
        output = model(images)  # виклик forward
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1} completed.")

