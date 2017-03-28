


confusion = confusion_matrix(predictions, y_test)
print(confusion)
invert_colors = np.ones(confusion.shape) * confusion.max()
plt.matshow(invert_colors - confusion)
plt.title('Confusion matrix')
plt.gray()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()


