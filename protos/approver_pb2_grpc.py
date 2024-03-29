# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import approver_pb2 as protos_dot_approver__pb2


class ApproverServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetApprover = channel.unary_unary(
                '/approver.ApproverService/GetApprover',
                request_serializer=protos_dot_approver__pb2.GetApproverRequest.SerializeToString,
                response_deserializer=protos_dot_approver__pb2.GetApproverResponse.FromString,
                )


class ApproverServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetApprover(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApproverServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetApprover': grpc.unary_unary_rpc_method_handler(
                    servicer.GetApprover,
                    request_deserializer=protos_dot_approver__pb2.GetApproverRequest.FromString,
                    response_serializer=protos_dot_approver__pb2.GetApproverResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'approver.ApproverService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ApproverService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetApprover(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/approver.ApproverService/GetApprover',
            protos_dot_approver__pb2.GetApproverRequest.SerializeToString,
            protos_dot_approver__pb2.GetApproverResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
