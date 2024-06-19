import torch


def multiclass_cross_entropy(predictions, labels):

    if len(labels.shape) == 1:
        labels = torch.nn.functional.one_hot(labels, num_classes=predictions.shape[1])

    # clipping the predictions
    eps = 1e-12
    predictions = torch.clamp(prediction, min=eps, max=1 - eps)


    loss = -torch.sum(labels * torch.log(prediction), dim=1)
    print(loss)
    return torch.mean(loss)

if __name__ == "__main__":
    batch_size = 10
    num_classes = 4
    prediction = torch.rand(batch_size, num_classes)
    labels = torch.randint(0, num_classes, (batch_size,))

    print("returned output", multiclass_cross_entropy(prediction, labels))

    # print("Prediction", prediction)
    # print("labels", labels)

