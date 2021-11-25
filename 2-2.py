if __name__=='__main__':
    file = open('data.txt', 'r')
    file_content = file.read()
    file.close()

    file_to_write = open('new_data.txt', 'w')
    file_to_write.writelines(file_content)
    file_to_write.close()

    with open('new_data.txt', 'a') as file_to_write:
        file_to_write.write('\nhello')