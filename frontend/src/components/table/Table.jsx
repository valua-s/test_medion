import { CheckCircleOutlined, CloseCircleOutlined } from '@ant-design/icons';

export const columns = [
  {
    title: 'Фамилия',
    dataIndex: 'last_name',
    key: 'last_name',
  },
  {
    title: 'Имя',
    dataIndex: 'first_name',
    key: 'first_name',
  },
  {
    title: 'Отчество',
    dataIndex: 'patronymic',
    key: 'patronymic',
  },
  {
    title: 'Должность',
    dataIndex: 'position',
    key: 'position',
    render: (text, record) => {
      return record.position ? record.position.name : "-"; // Проверяем значение position
    },
  },
  {
    title: 'Уволен',
    dataIndex: 'is_fired',
    key: 'is_fired',
    render: (isFired) => {
      return isFired ? <CheckCircleOutlined style={{ color: '#8b0000' }} /> : <CloseCircleOutlined style={{ color: '#4CAF50' }} />;
    },
  },
  {
    title: 'Дата увольнения',
    dataIndex: 'fire_date',
    key: 'fire_date',
  },
];
